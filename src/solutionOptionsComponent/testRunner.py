import sympy as *
import pandas as pd
import json
import sys
import os
import determineFunction as *
import evaluateEmissions as *

determineFunction("dataFiles/current_user_data.json")
print(evaluateEmissions("dataFiles/current_user_data.json", 12)) 
