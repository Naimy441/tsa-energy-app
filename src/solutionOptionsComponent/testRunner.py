import json
from sympy as *

with open("dataFiles/current_user_data.json", "r") as user_data:
    jsonUserData = json.load(user_data)
