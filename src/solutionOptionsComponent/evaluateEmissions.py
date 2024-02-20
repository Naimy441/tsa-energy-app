import json
import sympy as *

def evaluateEmissions(json_file_name, time_in_months):
  with open("json_file_name", "r") as user_data:
      jsonUserData = json.load(user_data)

  func = sympify(jsonUserData["CO2 Function"])
  func = func.subs(sh_time, jsonUserData["Consumption information"]["Space Heating"][1])
  func = func.subs(wh_time, jsonUserData["Consumption information"]["Water Heating"][1])
  func = func.subs(ac_time, jsonUserData["Consumption information"]["Air conditioning"][1])
  func = func.subs(refrigerators_time, jsonUserData["Consumption information"]["Refrigerators"][1])
  func = func.subs(other_time, jsonUserData["Consumption information"]["Other"][1])

  return func*(time_in_months)/12
  
