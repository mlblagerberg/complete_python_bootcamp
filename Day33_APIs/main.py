"""Project: APIs ISS Location
Start: May 21st, 2024
Last touched: May 21st, 2024
Author: Madeleine L.
"""
import requests
from datetime import datetime, timezone
import time
import math

LAT = 47.037872
LONG = -122.900696
# HEIGHT_ABOVE_SEA = 61  # feet: 201 meters: 61
# EARTH_RADIUS = 6371000  # in meters
# HEIGHT = 1.75  # in meters
# PERCENT_SKY = 0.60

# If the ISS is close to my current position and it is dark out
# Run code every 60 seconds then send an email


def is_night():
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
    now = datetime.now(timezone.utc)
    if sunset_hour <= now.hour <= sunrise_hour:
        return True, now
    else:
        return False, now

# # Estimate visible sky
# horizon_distance = (2*EARTH_RADIUS*HEIGHT) ** (1 / 2)
# visible_sky = horizon_distance*PERCENT_SKY


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    lat_long = [latitude, longitude]
    if LAT-5 <= latitude <= LAT+5 and LONG-5 <= longitude <= LONG+5:
        return True, lat_long
    else:
        return False, lat_long

# # Calculate distance to ISS from current lat/long
# gcd = EARTH_RADIUS * math.acos(
#     (math.cos(LAT) * math.cos(latitude) * math.cos(LONG - longitude)) +
#     (math.sin(LAT) * math.sin(latitude)))
# print(gcd)


while True:
    overhead, lat_long = iss_overhead()
    night, now = is_night()
    if night and overhead:
        time.sleep(1500)
        with open("ISS_log.txt", "a") as iss_log:
            iss_log.write(f"At {now} the ISS should be visible in the sky at latitude: {lat_long[0]} and longitude: "
                          f"{lat_long[1]}\n")
    else:
        with open("ISS_log.txt", "a") as iss_log:
            iss_log.write(f"At {now} the ISS is NOT visible at latitude: {lat_long[0]} and longitude: {lat_long[1]}\n")


