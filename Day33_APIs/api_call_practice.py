"""Project: APIs Practice
Start: May 21st, 2024
Last touched: May 21st, 2024
Author: Madeleine L.
"""
# Resources: HTTP Status Code Glossary https://www.webfx.com/web-development/glossary/http-status-codes/

# Application Program Interfaces (APIs): is a set of commands, protocols, and objects that programmers can use to create
# software or interact with an external system

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)  # Default is to get the response code
# Response Codes Review -
# 1XX: Hold on, something is happening
# 2XX: Here you go, everything worked as expected
# 3XX: You don't have permission to get this
# 4XX: You screwed up. What you are looking for does not exist
# 5XX: I screwed up (server is down or some other access issue on the websites side of things.)
# print(response.status_code)
response.raise_for_status()
data = response.json()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
lat_long = [latitude, longitude]
print(lat_long)




