"""Project: APIs ISS Location
Start: May 21st, 2024
Last touched: May 21st, 2024
Author: Madeleine L.
"""
import requests
from datetime import datetime
import math

LAT = 47.037872
LONG = -122.900696
# HEIGHT_ABOVE_SEA = 61  # feet: 201 meters: 61
EARTH_RADIUS = 6371000  # in meters
HEIGHT = 1.75  # in meters
PERCENT_SKY = 0.60

# If the ISS is close to my current position and it is dark out
# Run code every 60 seconds then send an email

# API input parameters
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

# Estimate visible sky
horizon_distance = (2*EARTH_RADIUS*HEIGHT) ** (1 / 2)
visible_sky = horizon_distance*PERCENT_SKY

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
latitude = float(data["iss_position"]["latitude"])
longitude = float(data["iss_position"]["longitude"])
lat_long = [latitude, longitude]
print(latitude)
print(longitude)
# Calculate distance to ISS from current lat/long
gcd = EARTH_RADIUS * math.acos(
    (math.cos(LAT) * math.cos(latitude) * math.cos(LONG - longitude)) +
    (math.sin(LAT) * math.sin(latitude)))
print(gcd)
if sunset_hour < hour_now.hour < sunrise_hour:
    print("Night time.")
    if gcd <= visible_sky:
        print("ISS is visible")
else:
    print("Day time")

