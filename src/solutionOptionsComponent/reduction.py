import sympy as *
import json
import determineFunction as *

with open ("dataFiles/current_user_data.json", "r") as file:
    jsonData1 = json.load(file)

with open("dataFiles/potential_user_data.json", "r") as file2:
    jsonData2 = json.load(file2)
    jsonData2["Statistics"]= jsonData1["Statistics"]
    jsonData2["Consumption information"] = jsonData1["Consumption information"]
    jsonData2["CO2 Function"] = jsonData1["CO2 Function"]
    newData  = json.dumps(jsonData2, indent = 4)

determineFunction("dataFiles/potential_user_data.json")

with open("dataFiles/potential_user_data.json", "w") as file2:
    file2.write(newData)

with open("dataFiles/potential_user_data.json", "r") as file3:
    jsonUserData = json.load(file3)

func0 = sympify(jsonUserData["CO2 Function"])

func0 = func0.subs(sh_time, jsonUserData["Consumption information"]["Space heating"][1])
func0 = func0.subs(wh_time, jsonUserData["Consumption information"]["Water heating"][1])
func0 = func0.subs(ac_time, jsonUserData["Consumption information"]["Air conditioning"][1])
func0 = func0.subs(refrigerators_time, jsonUserData["Consumption information"]["Refrigerators"][1])
func0 = func0.subs(other_time, jsonUserData["Consumption information"]["Other"][1])

func0 = (1 - jsonUserData["Reduction information"]["Target reduction"]/100)*func0

func = sympify(jsonUserData["CO2 Function"])

list = ["Space heating", "Water heating", "Air conditioning", "Refrigerators", "Other"]
varList = [sh_time, wh_time, ac_time, refrigerators_time, other_time]
changeIndexList = []

for i in range(len(list)):
  fuelType = list[i]
  notInList = true
  for var in jsonUserData["Reduction information"]["Variables to reduce"]:
    if (var[0] == fuelType):
      notInList = false
  if (notInList):
    func = func.subs(varList[i], jsonUserData["Consumption information"][fuelType][1])
  else:
    changeIndexList.append(i)
    
dist = 0
for index in changeIndexList:
  fuelType = list[index]
  origVal = jsonUserData["Consumption information"][fuelType][1]
  dist = dist + (varList[i] - origVal)**2

functionToOptimize = (func - func0)**2 + dist

#print(functionToOptimize)


    
    
  

