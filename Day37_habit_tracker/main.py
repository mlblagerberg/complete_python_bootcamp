"""Project: Habit Tracker - Daily Movement Graph
Start: July 1st, 2024
Last touched: August 6th, 2024
Author: Madeleine L.
"""

import os
import requests

TOKEN = os.getenv("PIXELA_TOKEN")
USER = "madeleine"

# Resources: Pixela - https://pixe.la/

# Definitions:
# get: pull something from external service
# post: pushes something to external service
# put: updates something in external service
# delete: remove something from external service

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

user_parameters = {
    "token": TOKEN,
    "user": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

graph_config = {
    "id": "movementgraph1",
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


