import json
from sympy import *
from determineFunction import determineFunction

x,t = symbols("x t")

determineFunction()

with open("dataFiles/current_user_data.json", "r") as user_data:
    jsonUserData = json.load(user_data)

array1 = []
array2 = []

for i in range(60):
    array1.append([i, float(sympify(jsonUserData["CO2 Function"]).subs(t, i/12))])
    array2.append([i, float(sympify(jsonUserData["CO2 Accumulation Function"]).subs(x, i/12))])

with open ("dataFiles/current_user_data.json", "r") as f:
  jsonData = json.load(f)
  jsonData["ipcData1"] = array1
  jsonData["ipcData2"] = array2
  newData  = json.dumps(jsonData, indent = 4)

with open("dataFiles/current_user_data.json", "w") as file2:
  file2.write(newData)
  
# Outputs the response to the user in JSON format
print(json.dumps({"chartLists" : {"ipcData1" : array1, "ipcData2" : array2}}))

    
