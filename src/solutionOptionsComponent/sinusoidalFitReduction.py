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

  #print(os.listdir())
  t, maxshtime, minshtime, averagesh, maxwhtime, minwhtime, averagewh, maxactime, minactime, averageac = symbols("t macshtime minshtime averagesh maxwhtime minwhtime averagewh maxactime minactime averageac")
  
  with open("dataFiles\current_user_data.json", "r") as user_data:
    jsonUserData = json.load(user_data)


  #SPACE HEATING
  maxshmonth = jsonUserData["Consumption information"]["Space heating"][1][0]
  maxshmonth = DICTIONARY[maxshmonth]

  minshmonth = jsonUserData["Consumption information"]["Space heating"][2][0]
  minshmonth = DICTIONARY[minshmonth]

  averagesh = (maxshtime + minshtime) / 2

  totalshtime = averagesh + ((maxshtime - averagesh) * cos(2*pi*(t - maxshmonth)))

  

  #WATER HEATING
  maxwhmonth = jsonUserData["Consumption information"]["Water heating"][1][0]
  maxwhmonth = DICTIONARY[maxwhmonth]
  
  minwhmonth = jsonUserData["Consumption information"]["Water heating"][2][0]
  minwhmonth = DICTIONARY[minwhmonth]

  
  averagewh = (maxwhtime + minwhtime) / 2

  totalwhtime = averagewh + ((maxwhtime - averagewh) * cos(2*pi*(t - maxwhmonth)))


  #AIR CONDITIONING
  maxacmonth = jsonUserData["Consumption information"]["Air conditioning"][1][0]
  maxacmonth = DICTIONARY[maxacmonth]
  
  minacmonth = jsonUserData["Consumption information"]["Air conditioning"][2][0]
  minacmonth = DICTIONARY[minacmonth]

  
  averageac = (maxactime + minactime) / 2

  totalactime = averageac + ((maxactime - averageac) * cos(2*pi*(t - maxacmonth)) )

  #print(str(totalshtime))
  #print(str(totalwhtime))
  #print(str(totalactime))
                             
  return [str(totalshtime), str(totalwhtime), str(totalactime)]
