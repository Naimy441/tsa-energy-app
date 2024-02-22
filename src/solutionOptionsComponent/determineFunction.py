from sympy import *
from sympy import Array
import math
import pandas as pd
import json
import sys

def determineFunction(jsonFileName):
  jsonFileName = jsonFileName
  with open(jsonFileName, "r") as user_data:
    jsonUserData = json.load(user_data)
  with open("dataFiles/constants.json", "r") as constants:
    jsonConstants = json.load(constants)
  sh_consumption, sh_time, wh_consumption, wh_time, ac_consumption, ac_time, refrigerators_consumption, refrigerators_time, other_consumption, other_time= symbols("sh_consumption sh_time wh_consumption wh_time ac_consumption ac_time refrigerators_consumption refrigerators_time other_consumption other_time")
  TOTAL_CONSUMPTION_PER_HOUSE = jsonConstants["Total consumption per house"]
  ELECTRICITY_CONVERSION_FACTOR = jsonConstants["Carbon constants"]["Electricity"]
  NATURAL_GAS_CONVERSION_FACTOR = jsonConstants["Carbon constants"]["Natural gas"]
  FUEL_OIL_OR_KEROSENE_CONVERSION_FACTOR = jsonConstants["Carbon constants"]["Fuel oil or kerosene"]
  PROPANE_CONVERSION_FACTOR = jsonConstants["Carbon constants"]["Propane"]
  WOOD_CONVERSION_FACTOR = jsonConstants["Carbon constants"]["Wood"]

  Conversion_Factors = [ ["Electricity", ELECTRICITY_CONVERSION_FACTOR], ["Natural gas", NATURAL_GAS_CONVERSION_FACTOR], ["Fuel oil or kerosone", FUEL_OIL_OR_KEROSENE_CONVERSION_FACTOR], ["Propane", PROPANE_CONVERSION_FACTOR], ["Wood", WOOD_CONVERSION_FACTOR]]

  SH_HOURS_PER_DAY = jsonConstants["Normal hours per day"]["Space heating"]
  WH_HOURS_PER_DAY = jsonConstants["Normal hours per day"]["Water heating"]
  AC_HOURS_PER_DAY = jsonConstants["Normal hours per day"]["Air conditioning"]
  REFRIGERATORS_HOURS_PER_DAY = jsonConstants["Normal hours per day"]["Refrigerators"]
  OTHER_CONSUMPTION_HOURS_PER_DAY = jsonConstants["Normal hours per day"]["Other"]

  Consumption_Hours = [SH_HOURS_PER_DAY, WH_HOURS_PER_DAY, AC_HOURS_PER_DAY, REFRIGERATORS_HOURS_PER_DAY, OTHER_CONSUMPTION_HOURS_PER_DAY] 

  #DEFINED THE DATA SET HERE
  EnergyData = pd.read_csv(r"C:\Users\masia\OneDrive\Documents\tsa-energy-app-main\tsa-energy-app-main\src\solutionOptionsComponent\ce3.1 (1).xlsx - EnergyData (1).csv")

  housing_unit_type = jsonUserData["Statistics"]["Housing unit type"]
  ownership = jsonUserData["Statistics"]["Ownership of housing unit"]
  year_of_construction = jsonUserData["Statistics"]["Year of construction"]
  square_footage = jsonUserData["Statistics"]["Total square footage"]
  num_of_household_members = jsonUserData["Statistics"]["Number of household members"]
  household_income = jsonUserData["Statistics"]["2020 annual household income"]
  payment_method = jsonUserData["Statistics"]["Payment method for energy bills"]

  statsArray = [["Housing unit type", housing_unit_type], ["Ownership of housing unit", ownership], ["Year of construction", year_of_construction], ["Total square footage", square_footage], ["Number of household members", num_of_household_members], ["2020 annual household income", household_income], ["Payment method for energy bills", payment_method]]

  arrayOfFuels =  [ ["Space heating", "", 1 ],  ["Water heating", "", 1 ], ["Air conditioning", "", 1], ["Refrigerators", "", 1 ], ["Other", "", 1 ]] 
  symbolsOfFuels = [sh_consumption, wh_consumption, ac_consumption, refrigerators_consumption, other_consumption]


  coefficient = 1
  func = coefficient*(sh_consumption * sh_time + wh_consumption * wh_time + ac_consumption * ac_time + refrigerators_consumption * refrigerators_time + other_consumption*other_time)
  var = func

  for fuel in arrayOfFuels:
    fuel[1] = jsonUserData["Consumption information"][fuel[0]][0]
    fuel[2] = jsonUserData["Consumption information"][fuel[0]][1]

  for i in range(len(statsArray)):
    for j in EnergyData.index:
      if (EnergyData.loc[j, "Category"] == statsArray[i][1]):
        average_energy_site_consumption = float(EnergyData.loc[j, "Total"])

    #print(statsArray[i][1] + ": " + str(average_energy_site_consumption))
    factor = average_energy_site_consumption/TOTAL_CONSUMPTION_PER_HOUSE
    coefficient = coefficient*factor

  for i in range(len(arrayOfFuels)):
    fuel = arrayOfFuels[i]
    #print(fuel[1])
    for j in EnergyData.index:
      #print(EnergyData.loc[j, "Category"])
      if (EnergyData.loc[j, "Category"] == fuel[1]):
        average_energy_fuel_consumption = float(EnergyData.loc[j, fuel[0]])
        #print(fuel[1] + ": " + str(average_energy_fuel_consumption))
    summand = (average_energy_fuel_consumption/(Consumption_Hours[i]))
    for factor in Conversion_Factors:
      if (fuel[1] == factor[0]):
        summand = summand*factor[1]
      var = var.subs(symbolsOfFuels[i], summand)

  var = str(var)

  with open (jsonFileName, "r") as file:
    jsonData = json.load(file)
    jsonData["CO2 Function"] = var
    newData  = json.dumps(jsonData, indent = 4)

  with open(jsonFileName, "w") as file2:
    file2.write(newData)
