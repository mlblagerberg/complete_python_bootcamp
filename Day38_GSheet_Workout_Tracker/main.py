"""Project: Workout Tracker
Start: August 6th, 2024
Last touched: August 6th, 2024
Author: Madeleine L.
"""


import requests
import os
from datetime import datetime

API_KEY = os.getenv("NUTRITIONIX_APP_ID")
APP_ID = os.getenv("NUTRITIONIX_API_KEY")

# Resources: https://www.nutritionix.com/business/api
