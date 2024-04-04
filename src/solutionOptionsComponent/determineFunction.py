import pandas as pd
from sympy import *
import json
from pathlib import Path
from sinusoidalFit import sinusoidalFit

def determineFunction():
  with open("dataFiles/current_user_data.json", "r") as user_data:
    jsonUserData = json.load(user_data)
  with open("dataFiles/constants.json", "r") as constants:
    jsonConstants = json.load(constants)
  x, t, sh_consumption, sh_time, wh_consumption, wh_time, ac_consumption, ac_time, refrigerators_consumption, refrigerators_time, other_consumption, other_time= symbols("x t sh_consumption sh_time wh_consumption wh_time ac_consumption ac_time refrigerators_consumption refrigerators_time other_consumption other_time")
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

  # DEFINED THE DATA SET HERE
  energyDataPathObject = Path("src/solutionOptionsComponent/energyData.csv").absolute()
  EnergyData = pd.read_csv(energyDataPathObject.resolve())

  housing_unit_type = jsonUserData["Statistics"]["Housing unit type"]
  year_of_construction = jsonUserData["Statistics"]["Year of construction"]
  square_footage = jsonUserData["Statistics"]["Total square footage"]
  num_of_household_members = jsonUserData["Statistics"]["Number of household members"]
  household_income = jsonUserData["Statistics"]["2020 annual household income"]
  payment_method = jsonUserData["Statistics"]["Payment method for energy bills"]

  statsArray = [["Housing unit type", housing_unit_type], ["Year of construction", year_of_construction], ["Total square footage", square_footage], ["Number of household members", num_of_household_members], ["2020 annual household income", household_income], ["Payment method for energy bills", payment_method]]

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
    #TEST1
    #print(coefficient)

  for i in range(len(arrayOfFuels)):
    fuel = arrayOfFuels[i]
    #print("\n" + fuel[0] + ":")
    #print("Fuel: " + fuel[1])
    #print(fuel[1])
    for j in EnergyData.index:
      #print(EnergyData.loc[j, "Category"])
      if (EnergyData.loc[j, "Category"] == fuel[1]):
        average_energy_fuel_consumption = float(EnergyData.loc[j, fuel[0]])
        #print("Average Energy Fuel Consumption " + str(average_energy_fuel_consumption))
        #TEST2////////
        #print(fuel[1] + ": " + str(average_energy_fuel_consumption) + ", " + str(Consumption_Hours[i]))
    summand = (average_energy_fuel_consumption/(Consumption_Hours[i]))
    for factor in Conversion_Factors:
      if (fuel[1] == factor[0]):
        #print(summand, factor[1])
        summand = summand*factor[1]
    var = var.subs(symbolsOfFuels[i], summand)
    #print("Summand: " + str(summand))
    #print("Final Yearly Emissions: " + str(summand*Consumption_Hours[i]))
      

    
  sineList = sinusoidalFit()
  var = (var.subs(sh_time, sympify(sineList[0]))).subs(wh_time, sympify(sineList[1])).subs(ac_time, sympify(sineList[2]))
  var = var.subs(refrigerators_time, jsonUserData["Consumption information"]["Refrigerators"][1])
  var = var.subs(other_time, jsonUserData["Consumption information"]["Other"][1])

  accumulateVar = integrate(var, (t, 0, x))


  var = str(var)
  #print(var)
  accumulateVar = str(accumulateVar)
  #print(accumulateVar)
  

  with open ("dataFiles/current_user_data.json", "r") as f:
    jsonData = json.load(f)
    jsonData["CO2 Function"] = var
    jsonData["CO2 Accumulation Function"] = accumulateVar
    newData  = json.dumps(jsonData, indent = 4)

  with open("dataFiles/current_user_data.json", "w") as file2:
    file2.write(newData)

