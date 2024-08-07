"""Project: Habit Tracker - Daily Movement Graph
Start: July 1st, 2024
Last touched: August 7th, 2024
Author: Madeleine L.
"""

import os
import requests
from datetime import datetime

TOKEN = os.getenv("PIXELA_TOKEN")
USER = "madeleine"
GRAPH_ID = "movementgraph1"

MINUTES = 0
DATE = datetime.today().strftime("%Y%m%d")

# Resources: Pixela - https://pixe.la/
# My graph - https://pixe.la/v1/users/madeleine/graphs/movementgraph1.html

# Definitions:
# get: pull something from external service
# post: pushes something to external service
# put: updates something in external service
# delete: remove something from external service

current_date = datetime.today().strftime("%Y%m%d")
# print(current_date)

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"
update_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{current_date}"

user_parameters = {
    "token": TOKEN,
    "user": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_config = {
    "id": GRAPH_ID,
    "name": "Movement Graph",
    "unit": "minutes",
    "type": "int",
    "color": "sora",
    "timezone": "America/Los_Angeles",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# Get existing pixel data to update
try:
    pixel_data = requests.get(url=update_endpoint, headers=headers)
    current_data = (int(pixel_data.json()["quantity"]))
except KeyError:
    current_data = 0

# print(current_data)
current_data += MINUTES
# print(current_data)


pixel_update = {
    "quantity": str(current_data),
}

response = requests.put(url=update_endpoint, json=pixel_update, headers=headers)
print(response.text)

# minutes = -10
# create_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"
#
# pixel_update = {
#     "date": "20240806",
#     "quantity": str(minutes),
# }
#
# response = requests.post(url=create_endpoint, json=pixel_update, headers=headers)
# print(response.text)

