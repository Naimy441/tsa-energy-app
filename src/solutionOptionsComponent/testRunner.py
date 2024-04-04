import json
from sympy as *
from determineFunction import determineFunction

with open("dataFiles/current_user_data.json", "r") as user_data:
    jsonUserData = json.load(user_data)
