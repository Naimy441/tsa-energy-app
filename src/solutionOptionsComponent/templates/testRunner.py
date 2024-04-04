tefrom sympy import *
import json
import sys
import os

from determineFunction import determineFunction
from evaluateEmissions import evaluateEmissions

# Gets the request from the user in JSON format
jsonArgs = json.loads(sys.argv[1])

sh_consumption, sh_time, wh_consumption, wh_time, ac_consumption, ac_time, refrigerators_consumption, refrigerators_time, other_consumption, other_time = symbols("sh_consumption sh_time wh_consumption wh_time ac_consumption ac_time refrigerators_consumption refrigerators_time other_consumption other_time")

currentWorkingDirectory = os.getcwd()

determineFunction(currentWorkingDirectory)

arr  = [] 
for t in range(60):
  arr.append([t, evaluateEmissions(t)])

# Outputs the response to the user in JSON format
print(json.dumps({"chartList": arr}))
