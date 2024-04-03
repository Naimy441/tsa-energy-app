import pandas as pd
from sympy import *
import json
from pathlib import Path
from sinusoidalFit import sinusoidalFit

def determineFunction(CWD):
   with open("dataFiles/current_user_data.json", "r") as user_data:
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

  # DEFINED THE DATA SET HERE
  energyDataPathObject = Path("src/solutionOptionsComponent/energyData.csv").absolute()
  EnergyData = pd.read_csv(energyDataPathObject.resolve())

  housing_unit_type = jsonUserData["Statistics"]["Housing unit type"]
  year_of_construction = jsonUserData["Statistics"]["Year of construction"]
  square_footage = jsonUserData["Statistics"]["Total square footage"]
  num_of_household_members = jsonUserData["Statistics"]["Number of household members"]
  household_income = jsonUserData["Statistics"]["2020 annual household income"]
  payment_method = jsonUserData["Statistics"]["Payment method for energy bills"]
