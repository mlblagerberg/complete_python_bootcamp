"""Project: API Auth - SMS Rain Alert
Start: May 26th
Last touched: May 30th, 2024
Author: Madeleine L.
"""
# Resources:
# https://home.openweathermap.org/users/sign_up
import requests
import sys
sys.path.append("/Users/madeleinebeattylagerberg/GitHub/complete_python_bootcamp")
from api_keys import WEATHER_API, LAT, LONG

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={WEATHER_API}"

response = requests.get(url=URL)
print(response.text)
