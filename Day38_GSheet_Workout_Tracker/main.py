"""Project: Workout Tracker
Start: August 6th, 2024
Last touched: August 7th, 2024
Author: Madeleine L.
"""

# Resources:
# API - https://www.nutritionix.com/business/api
# NLP Exercise documentation - https://docx.syndigo.com/developers/docs/natural-language-for-exercise

import requests
import os
from datetime import datetime

APP_ID = os.getenv('NUTRITIONIX_APP_ID')
API_KEY = os.getenv('NUTRITIONIX_API_KEY')
SHEETY_AUTH = os.getenv('SHEETY_AUTH')

WEIGHT_KG = 90
HEIGHT_CM = 175.26
AGE = 37
GENDER = "female"

input_text = input("Tell me which exercise you did: ")

# Exercise NLP Endpoint
nlp_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    'Content-Type': 'application/json',
}

parameters = {
    "query": input_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nlp_endpoint, json=parameters, headers=headers)

try:
    response.raise_for_status()
    response = response.json()["exercises"][0]
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")

# print(response)
exercise = response["name"]
duration_min = response["duration_min"]
calories = response["nf_calories"]

# print(exercise)
# print(duration_min)
# print(calories)

current_date = datetime.now().strftime("%Y/%m/%d")
current_time = datetime.now().strftime("%I:%M:%S")
# print(current_date)

# Google Sheet Endpoint
sheet_endpoint = "https://api.sheety.co/cb16434dc56835525f9150d06b23af49/trackedWorkouts/workouts"

workout_data = {
    "workout": {
        "date": current_date,
        "time": current_time,
        "exercise": exercise,
        "duration": duration_min,
        "calories": calories,
    }
}

headers = {
    'Authorization': f'Basic {SHEETY_AUTH}'
}

response = requests.post(url=sheet_endpoint, json=workout_data, headers=headers)
# print(response.json())




