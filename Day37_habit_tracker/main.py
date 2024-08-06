"""Project: Habit Tracker - Daily Weight lifting
Start: July 1st, 2024
Last touched: August 6th, 2024
Author: Madeleine L.
"""

import os
import requests

# Resources: Pixela - https://pixe.la/

# Definitions:
# get: pull something from external service
# post: pushes something to external service
# put: updates something in external service
# delete: remove something from external service

pixela_endpoint = "https://pixe.la/v1/users"

pixela_token = os.getenv("PIXELA_TOKEN")
# print(pixela_token)
# user_parameters = {
#     "token": pixela_token,
#     "username": "madeleine",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

