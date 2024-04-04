import json
from sympy import *

def evaluateEmissions(time_in_months):
  sh_consumption, sh_time, wh_consumption, wh_time, ac_consumption, ac_time, refrigerators_consumption, refrigerators_time, other_consumption, other_time= symbols("sh_consumption sh_time wh_consumption wh_time ac_consumption ac_time refrigerators_consumption refrigerators_time other_consumption other_time")
  with open("dataFiles/current_user_data.json", "r") as user_data:
      jsonUserData = json.load(user_data)

  func = sympify(jsonUserData["CO2 Function"])
  func = func.subs(sh_time, jsonUserData["Consumption information"]["Space heating"][1])
  func = func.subs(wh_time, jsonUserData["Consumption information"]["Water heating"][1])
  func = func.subs(ac_time, jsonUserData["Consumption information"]["Air conditioning"][1])
  func = func.subs(refrigerators_time, jsonUserData["Consumption information"]["Refrigerators"][1])
  func = func.subs(other_time, jsonUserData["Consumption information"]["Other"][1])

  return float(func)*(time_in_months)/12
