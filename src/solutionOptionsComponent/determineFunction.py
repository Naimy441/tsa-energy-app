from sympy import *
from sympy import Array
import math
import pandas as pd

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u ,v ,w, x, y, z = symbols("a b c d e f g h i j k l m n o p q r s t u v w x y z")

TOTAL_CONSUMPTION_PER_HOUSE = 76.8


housing_unit_type = input("Housing Unit Type: ")
ownership = input("Ownership: ")
year_of_construction = input("Year of Construction: ")
square_footage = input("Square Footage: ")
num_of_household_members = input("Number of Household Members: ")
household_income = input("Household Income: ") 
payment_method = input("Payment Method: ")

statsArray = [["Housing unit type", housing_unit_type], ["Ownership of housing unit", ownership], ["Year of construction", year_of_construction], ["Total square footage", square_footage], ["Number of household members", num_of_household_members], ["2020 annual household income", household_income], ["Payment method for energy bills", payment_method]]

arrayOfFuels =  [ ["Space Heating", "", 0 ],  ["Water Heating", "", 0 ], ["Air Conditioning", "", 0 ], ["Refrigerators", "", 0 ] ] 

for fuel in arrayOfFuels:
  fuel[1] = input("Type of Fuel for " + fuel[0] + ": ") 
  fuel[2] = int(input("Number of Hours per Day: "))

coefficient = 1
for i in range(statsArray):
  #Change
  average_energy_site_consumption = 1
  factor = average_energy_site_consumption*TOTAL_CONSUMPTION_PER_HOUSE
  coefficient = coefficient*factor


  
  
  
  





















