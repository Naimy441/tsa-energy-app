from sympy import *
from sympy.vector import CoordSys3D, gradient
import json
from determineFunction import *
from scipy.optimize import minimize
from scipy.optimize import *
from sympy.utilities.lambdify import lambdify

#with open ("dataFiles/current_user_data.json", "r") as file:
#    jsonData1 = json.load(file)


sh_consumption, sh_time, wh_consumption, wh_time, ac_consumption, ac_time, refrigerators_consumption, refrigerators_time, other_consumption, other_time= symbols("sh_consumption sh_time wh_consumption wh_time ac_consumption ac_time refrigerators_consumption refrigerators_time other_consumption other_time")

determineFunction("dataFiles/potential_user_data.json")

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
changeVarsList = []
for index in changeIndexList:
  fuelType = list[index]
  changeVarsList.append(varList[index])
  origVal = jsonUserData["Consumption information"][fuelType][1]
  dist = dist + (varList[index] - origVal)**2

functionToOptimize = abs(func - func0)

print(functionToOptimize)

changeVarsTuple = tuple(changeVarsList)
print(changeVarsTuple)
#is
NewFunctionToOptimize = lambdify(changeVarsTuple, functionToOptimize)
#is
def my_func_v(x):
  return NewFunctionToOptimize(*tuple(x))

#print(minimize(my_func_v,[0.1,0.1,0.1]))


#OPTIMIZE GIVEN CONSTRAINTS

#Extract constraints
constraintList = []
for index in changeIndexList:
  for smallList in jsonUserData["Reduction information"]["Variables to reduce"]:
    if (smallList[0] == list[index]):
      constraintList.append([smallList[1], smallList[2]])


#Defining Linear constraint
matrix = []
i = 0
for index in changeIndexList:
  row = []
  for jndex in changeIndexList:
    row.append(0)
  row[i] = 1
  matrix.append(row)
  i = i + 1
print(matrix)

lowerConstraintList = []
upperConstraintList= []
#is it
for constraints in constraintList:
  lowerConstraintList.append(constraints[0])
  upperConstraintList.append(constraints[1])

origValues = []
for index in changeIndexList:
  fuelType = list[index]
  origVal = jsonUserData["Consumption information"][fuelType][1]
  origValues.append(origVal)

linear_constraint = LinearConstraint(matrix, lowerConstraintList, upperConstraintList)

result = minimize(my_func_v, x0=origValues, constraints=[linear_constraint])

finalList = result.x
for i in range(len(changeIndexList)):
  index  = changeIndexList[i]
  fuelType = list[index]
  jsonUserData["Consumption information"][fuelType][1] = finalList[i]

newData  = json.dumps(jsonUserData, indent = 4)

with open("dataFiles/potential_user_data.json", "w") as file2:
  file2.write(newData)

