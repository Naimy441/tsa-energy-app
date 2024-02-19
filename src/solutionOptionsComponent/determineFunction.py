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


housing_unit_type = input("Housing Unit Type: ")
ownership = input("Ownership: ")
year_of_construction = input("Year of Construction: ")
square_footage = input("Square Footage: ")
num_of_household_members = input("Number of Household Members: ")
household_income = input("Household Income: ") 
payment_method = input("Payment Method: ")

statsArray = [["Housing unit type", housing_unit_type], ["Ownership of housing unit", ownership], ["Year of construction", year_of_construction], ["Total square footage", square_footage], ["Number of household members", num_of_household_members], ["2020 annual household income", household_income], ["Payment method for energy bills", payment_method]]

arrayOfFuels =  [ ["Space heating", "", 0 ],  ["Water heating", "", 0 ], ["Air conditioning", "", 0 ], ["Refrigerators", "", 0 ], ["Other", "", 0 ]] 

coefficient = 1
func = coefficient* (sh_consumption * sh_time + wh_consumption * wh_time + ac_consumption * ac_time + refrigerators_consumption * refrigerators_time + other_consumption*other_time)

for fuel in arrayOfFuels:
  fuel[1] = input("Type of Fuel for " + fuel[0] + ": ") 
  fuel[2] = int(input("Number of Hours per Day: "))

for i in range(statsArray):
  
  #Change below
  average_energy_site_consumption = 1
  #Change above
  
  factor = average_energy_site_consumption/TOTAL_CONSUMPTION_PER_HOUSE
  coefficient = coefficient*factor

 
  



  
  
  

  



















