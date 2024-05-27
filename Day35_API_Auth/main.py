"""Project: API Auth - SMS Rain Alert
Start: May 26th
Last touched: May 26h, 2024
Author: Madeleine L.
"""
# Resources:
# https://home.openweathermap.org/users/sign_up
import requests
import sys
sys.path.append("/Users/madeleinebeattylagerberg/GitHub/complete_python_bootcamp")
from api_keys import WEATHER_API

URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"