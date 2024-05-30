"""Project: API Auth - SMS Rain Alert
Start: May 26th
Last touched: May 30th, 2024
Author: Madeleine L.
"""
# Resources:
# https://home.openweathermap.org/users/sign_up
# https://openweathermap.org/forecast5
# https://jsonviewer.stack.hu/

import requests
import sys
sys.path.append("/Users/madeleinebeattylagerberg/GitHub/complete_python_bootcamp")
from constants_keys import WEATHER_API, LAT, LONG

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={WEATHER_API}"

response = requests.get(url=URL)
response.raise_for_status()
print(response)  # Default to print response code
data = response.json()
print(data)
print(data.keys())
