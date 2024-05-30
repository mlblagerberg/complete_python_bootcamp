"""Project: API Auth - SMS Rain Alert
Start: May 26th
Last touched: May 30th, 2024
Author: Madeleine L.
"""
# Resources:
# https://home.openweathermap.org/users/sign_up
# https://openweathermap.org/forecast5
# https://jsonviewer.stack.hu/
# https://openweathermap.org/weather-conditions # Condition ID definitions

import requests
import sys
sys.path.append("/Users/madeleinebeattylagerberg/GitHub/complete_python_bootcamp")
from constants_keys import WEATHER_API, LAT, LONG

FORECAST_COUNT = 4

# OWM_API_CURRENT_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={WEATHER_API}"
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast?"

parameters = {
    "lat": LAT,
    "lon": LONG,
    "appid": WEATHER_API,
    "cnt": FORECAST_COUNT
}


response = requests.get(url=OWM_API_ENDPOINT, params=parameters)
response.raise_for_status()
print(response)  # Default to print response code
data = response.json()
# print(data)
print(data.keys())

for forecast in range(len(data["list"])):
    weather = data["list"][forecast]["weather"]
    first_condition = weather[0]
    condition_id = first_condition["id"]
    if condition_id < 700:
        print("Bring an umbrella.")
    else:
        print("No umbrella needed.")

# print(data["list"][0]["weather"])  # Weather ID and description
