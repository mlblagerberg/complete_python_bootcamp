"""Project: APIs ISS Location
Start: May 21st, 2024
Last touched: May 24th, 2024
Author: Madeleine L.
"""
# Resources:
# https://sunrise-sunset.org/api
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/

import requests
from datetime import datetime, timezone
import time

LAT = 47.037872
LONG = -122.900696


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
    current_datetime = datetime.now(timezone.utc)
    if sunset_hour <= current_datetime.hour <= sunrise_hour:
        return True, current_datetime
    else:
        return False, current_datetime


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
