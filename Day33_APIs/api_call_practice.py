"""Project: APIs Practice
Start: May 21st, 2024
Last touched: May 21st, 2024
Author: Madeleine L.
"""
# Resources:
# HTTP Status Code Glossary https://www.webfx.com/web-development/glossary/http-status-codes/
# Sunrise/Sunset time API: https://sunrise-sunset.org/api

# Application Program Interfaces (APIs): is a set of commands, protocols, and objects that programmers can use to create
# software or interact with an external system

import requests
from datetime import datetime

LAT = 47.037872
LONG = -122.900696

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)  # Default is to get the response code
# # Response Codes Review -
# # 1XX: Hold on, something is happening
# # 2XX: Here you go, everything worked as expected
# # 3XX: You don't have permission to get this
# # 4XX: You screwed up. What you are looking for does not exist
# # 5XX: I screwed up (server is down or some other access issue on the websites side of things.)
# # print(response.status_code)
# response.raise_for_status()
# data = response.json()
# latitude = data["iss_position"]["latitude"]
# longitude = data["iss_position"]["longitude"]
# lat_long = [latitude, longitude]
# # print(lat_long)
#
# Required API input parameters
parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
 }

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])
hour_now = datetime.utcnow()

if sunset_hour < hour_now.hour < sunrise_hour:
    print("Night time.")
else:
    print("Day time")



