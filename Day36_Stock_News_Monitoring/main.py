"""Project: Stock News Monitor
Start: June 5th 2024
Last touched: June 5th, 2024
Author: Madeleine L.
"""

import requests
from datetime import datetime, timedelta
import os

api_key = os.getenv("ALPHA_VANTAGE_API")
# TODO 1: Get stock price delta between current day opening and previous day close
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "ENPH",
    "outputsize": "compact",
    "apikey": api_key,
}

url = "https://www.alphavantage.co/query?"
response = requests.get(url, params=parameters)
data = response.json()
# print(data)

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")

today_stock = data["Time Series (Daily)"][today]
yesterday_stock = data["Time Series (Daily)"][yesterday]
print(f"Today's stock details: {today_stock}")
print(f"Yesterday's stock details: {yesterday_stock}")

# TODO 2: If it was a large fluctuation (>10%) then find related news articles for company
# TODO 3: Send notification with fluctuation and any relevant articles

# # Resources
# Stock Price API: https://www.alphavantage.co/
# News API: https://newsapi.org/
# Twilio API: https://www.twilio.com/en-us

