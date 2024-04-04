from sympy import *
import json
import os

def sinusoidalFit():
  DICTIONARY = {
    "January": 1/12,
    "February": 2/12,
    "March": 3/12,
    "April": 4/12,
    "May": 5/12,
    "June": 6/12,
    "July": 7/12,
    "August": 8/12,
    "September": 9/12,
    "October": 10/12,
    "November": 11/12,
    "December": 1
  }

  print(os.listdir())
  t = symbols("t")
  
  with open("dataFiles\current_user_data.json", "r") as user_data:
    jsonUserData = json.load(user_data)


  #SPACE HEATING
  maxshtime = jsonUserData["Consumption information"]["Space heating"][1][1]
  maxshmonth = jsonUserData["Consumption information"]["Space heating"][1][0]
  maxshmonth = DICTIONARY[maxshmonth]

  minshtime = jsonUserData["Consumption information"]["Space heating"][2][1]
  minshmonth = jsonUserData["Consumption information"]["Space heating"][2][0]
  minshmonth = DICTIONARY[minshmonth]

  averagesh = (maxshtime + minshtime) / 2

  totalshtime = averagesh + ((maxshtime - averagesh) * cos(2*pi*(t - maxshmonth)))

  

  #WATER HEATING
  maxwhtime = jsonUserData["Consumption information"]["Water heating"][1][1]
  maxwhmonth = jsonUserData["Consumption information"]["Water heating"][1][0]
  maxwhmonth = DICTIONARY[maxwhmonth]
  
  minwhtime = jsonUserData["Consumption information"]["Water heating"][2][1]
  minwhmonth = jsonUserData["Consumption information"]["Water heating"][2][0]
  minwhmonth = DICTIONARY[minwhmonth]

  
  averagewh = (maxwhtime + minwhtime) / 2

  totalwhtime = averagewh + ((maxwhtime - averagewh) * cos(2*pi*(t - maxwhmonth)))


  #AIR CONDITIONING
  maxactime = jsonUserData["Consumption information"]["Air conditioning"][1][1]
  maxacmonth = jsonUserData["Consumption information"]["Air conditioning"][1][0]
  maxacmonth = DICTIONARY[maxacmonth]
  
  minactime = jsonUserData["Consumption information"]["Air conditioning"][2][1]
  minacmonth = jsonUserData["Consumption information"]["Air conditioning"][2][0]
  minacmonth = DICTIONARY[minacmonth]

  
  averageac = (maxactime + minactime) / 2

  totalactime = averageac + ((maxactime - averageac) * cos(2*pi*(t - maxacmonth)) )

  print(str(totalshtime))
  print(str(totalwhtime))
  print(str(totalactime))
                             
  return [str(totalshtime), str(totalwhtime), str(totalactime)]
  
  

sinusoidalFit()

  
  

  
