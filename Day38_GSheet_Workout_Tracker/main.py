"""Project: Workout Tracker
Start: August 6th, 2024
Last touched: August 6th, 2024
Author: Madeleine L.
"""

# Resources:
# API - https://www.nutritionix.com/business/api
# NLP Exercise documentation - https://docx.syndigo.com/developers/docs/natural-language-for-exercise

import requests
import os
from datetime import datetime

APP_ID = "d63b9126"  # os.getenv("NUTRITIONIX_APP_ID")
API_KEY = "6426eb5f0db8028f140de504b71fd6f8"  # os.getenv("NUTRITIONIX_API_KEY")
print(API_KEY)
WEIGHT_KG = 90
HEIGHT_CM = 175.26
AGE = 37
GENDER = "female"

input_text = input("Tell me which exercise you did: ")

nlp_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # 'Content-Type': 'application/json',
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
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
