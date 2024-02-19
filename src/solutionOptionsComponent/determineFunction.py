from sympy import *
from sympy import Array
import math
import pandas as pd

sh_consumption, sh_time, wh_consumption, wh_time, ac_consumption, ac_time, refrigerators_consumption, refrigerators_time, other_consumption, other_time= symbols("sh_consumption sh_time wh_consumption wh_time ac_consumption ac_time refrigerators_consumption refrigerators_time other_consumption other_time")

TOTAL_CONSUMPTION_PER_HOUSE = 76.8


#https://www.eia.gov/environment/emissions/co2_vol_mass.php
ELECTRICITY_CONVERSION_FACTOR = 379.63
NATURAL_GAS_CONVERSION_FACTOR = 116.65
FUEL_OIL_OR_KEROSENE_CONVERSION_FACTOR = 161.35
PROPANE_CONVERSION_FACTOR = 138.63
WOOD_CONVERSION_FACTOR = 2.5*116.65
SOME_OTHER_FUEL_CONVERSION_FACTOR = 116.65

Conversion_Factors = [ ["Electricity", ELECTRICITY_CONVERSION_FACTOR], ["Natural gas", NATURAL_GAS_CONVERSION_FACTOR], ["Fuel oil or kerosone", FUEL_OIL_OR_KEROSENE_CONVERSION_FACTOR], ["Propane", PROPANE_CONVERSION_FACTOR], ["Wood", WOOD_CONVERSION_FACTOR], ["Some other fuel", SOME_OTHER_FUEL_CONVERSION_FACTOR]]

SH_HOURS_PER_DAY = 8
WH_HOURS_PER_DAY = 4
AC_HOURS_PER_DAY = (35/60 * 14)
REFRIGERATORS_HOURS_PER_DAY = 8
OTHER_CONSUMPTION_HOURS_PER_DAY = 8

Consumption_Hours = [SH_HOURS_PER_DAY, WH_HOURS_PER_DAY, AC_HOURS_PER_DAY, REFRIGERATORS_HOURS_PER_DAY, OTHER_CONSUMPTION_HOURS_PER_DAY] 

housing_unit_type = input("Housing Unit Type: ")
ownership = input("Ownership: ")
year_of_construction = input("Year of Construction: ")
square_footage = input("Square Footage: ")
num_of_household_members = input("Number of Household Members: ")
household_income = input("Household Income: ") 
payment_method = input("Payment Method: ")

statsArray = [["Housing unit type", housing_unit_type], ["Ownership of housing unit", ownership], ["Year of construction", year_of_construction], ["Total square footage", square_footage], ["Number of household members", num_of_household_members], ["2020 annual household income", household_income], ["Payment method for energy bills", payment_method]]

arrayOfFuels =  [ ["Space heating", "", 1 ],  ["Water heating", "", 1 ], ["Air conditioning", "", 1], ["Refrigerators", "", 1 ], ["Other", "", 1 ]] 
symbolsOfFuels = [sh_consumption, wh_consumption, ac_consumption, refrigerators_consumption, other_consumption]


coefficient = 1
func = coefficient*(sh_consumption * sh_time + wh_consumption * wh_time + ac_consumption * ac_time + refrigerators_consumption * refrigerators_time + other_consumption*other_time)
var = func

for fuel in arrayOfFuels:
  fuel[1] = input("Type of Fuel for " + fuel[0] + ": ") 
  fuel[2] = int(input("Number of Hours per Day: "))

for i in range(len(statsArray)):

  #Change below
  average_energy_site_consumption = TOTAL_CONSUMPTION_PER_HOUSE
  #Change above

  factor = average_energy_site_consumption/TOTAL_CONSUMPTION_PER_HOUSE
  coefficient = coefficient*factor

for i in range(len(arrayOfFuels)):
  fuel = arrayOfFuels[i]
  average_energy_site_consumption = 1
  summand = (average_energy_site_consumption/(Consumption_Hours[i]))
  for factor in Conversion_Factors:
    if (fuel[1] == factor[0]):
      summand = summand*factor[1]
  var = var.subs(symbolsOfFuels[i], summand)

print(var)
print(coefficient)
print(var/coefficient)

  
  
  

  



















