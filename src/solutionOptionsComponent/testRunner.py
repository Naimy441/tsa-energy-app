from sympy import *
import pandas as pd
import json
import sys
import os
from determineFunction import *
from evaluateEmissions import *
import os

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))

sh_consumption, sh_time, wh_consumption, wh_time, ac_consumption, ac_time, refrigerators_consumption, refrigerators_time, other_consumption, other_time = symbols("sh_consumption sh_time wh_consumption wh_time ac_consumption ac_time refrigerators_consumption refrigerators_time other_consumption other_time")

determineFunction("dataFiles/current_user_data.json")

list = [] 
for (t in range(60)):
  list.append([t, evaluateEmissions("dataFiles/current_user_data.json", 12)])

