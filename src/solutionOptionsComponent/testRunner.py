import sympy as *
import pandas as pd
import json
import sys
import os
import determineFunction as *
import evaluateEmissions as *
sh_consumption, sh_time, wh_consumption, wh_time, ac_consumption, ac_time, refrigerators_consumption, refrigerators_time, other_consumption, other_time = symbols("sh_consumption sh_time wh_consumption wh_time ac_consumption ac_time refrigerators_consumption refrigerators_time other_consumption other_time")

determineFunction("dataFiles/current_user_data.json")
print(evaluateEmissions("dataFiles/current_user_data.json", 12)) 
