"""Project: API Auth - Short Messaging Service (SMS) Rain Alert
Start: May 26th
Last touched: June 4th, 2024
Author: Madeleine L.
"""
# Resources:
# https://home.openweathermap.org/users/sign_up
# https://openweathermap.org/forecast5
# https://jsonviewer.stack.hu/
# https://openweathermap.org/weather-conditions # Condition ID definitions
# https://console.twilio.com/?frameUrl=%2Fconsole%3Fx-target-region%3Dus1
# Other APIs to explore: https://apilist.fun/

import requests
import sys
import os
from twilio.rest import Client
sys.path.append("/Users/madeleinebeattylagerberg/GitHub/complete_python_bootcamp")

FORECAST_COUNT = 4

# OWM_API_CURRENT_WEATHER = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={WEATHER_API}"
OWM_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast?"
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
lat = os.environ.get("OLY_LAT")
long = os.environ.get("OLY_LONG")

weather_api_key = os.environ.get("WEATHER_API")

parameters = {
    "lat": lat,
    "lon": long,
    "appid": weather_api_key,
    "cnt": FORECAST_COUNT
}


response = requests.get(url=OWM_API_ENDPOINT, params=parameters)
response.raise_for_status()
# print(response)  # Default to print response code
data = response.json()
# print(data)
# print(data.keys())

for forecast in range(len(data["list"])):
    weather = data["list"][forecast]["weather"]
    first_condition = weather[0]
    condition_id = first_condition["id"]
    if condition_id < 700:
        rain = True
client = Client(ACCOUNT_SID, AUTH_TOKEN)

if rain:
    # print(f"{first_condition['main']}: Bring an umbrella.")
    message = client.messages.create(body= "It's going to rain today. Remember an ☔️",
                                     from_="+18336402577",
                                     to="+13604906012"
                                     )


# print(message.status)
# print(data["list"][0]["weather"])  # Weather ID and description
# Test logic
# list = [4, 5, 3, 6]
# for num in list:
#     if num < 5:
#         less = True
#
# if less:
#     print("value is less than 5")
# else:
#     print("Not less than 5")