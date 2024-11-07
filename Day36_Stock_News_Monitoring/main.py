"""Project: Stock News Monitor
Start: June 5th, 2024
Last touched: November 7th, 2024
Author: Madeleine L.
"""

import requests
from datetime import datetime, timedelta
import os
from json import dumps

# # Resources
# Stock Price API: https://www.alphavantage.co/
# News API: https://newsapi.org/
# Twilio API: https://www.twilio.com/en-us

stock_api_key = os.getenv("ALPHA_VANTAGE_API")
# print(stock_api_key)
# Get stock price delta between current day opening and previous day close
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "ENPH",
    "outputsize": "compact",
    "apikey": stock_api_key,
}

stock_url = "https://www.alphavantage.co/query?"
response = requests.get(stock_url, params=stock_parameters)
stock_data = response.json()
# print(stock_data)

# print(datetime.now())
latest_date_str = max(stock_data["Time Series (Daily)"])  # Save string so that it can be referenced when calling API
# print(latest_date_str)
latest_date = datetime.strptime(latest_date_str, "%Y-%m-%d")   # Convert string to datetime to do datetime math
# print(latest_date)
yesterday = (latest_date - timedelta(1)).strftime("%Y-%m-%d")
week_ago = (latest_date - timedelta(7)).strftime("%Y-%m-%d")

latest_stock = stock_data["Time Series (Daily)"][latest_date_str]
previous_day_stock = stock_data["Time Series (Daily)"][yesterday]
#
print(f"Most current day ({latest_date}) stock details: {latest_stock}")
print(f"Previous day ({yesterday}) stock details: {previous_day_stock}")
# print(f"Yesterday's stock details: {yesterday_stock}")
open_price = float(latest_stock["1. open"])
close_price = float(previous_day_stock["4. close"])
price_delta = close_price - open_price
print(round((price_delta/close_price)*100, 2))

if round((price_delta/close_price)*100, 2) >= 10:
    # If it was a large fluctuation (>10%) then find related news articles for company from the past week
    news_api_key = os.getenv("NEWS_API")

    news_url = "https://newsapi.org/v2/everything?"

    news_parameters = {
        "q": "ENPH",
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": news_api_key,
    }

    news_response = requests.get(news_url, params=news_parameters)
    news_data = news_response.json()
    # print(dumps(news_data))
    # print(news_data)

# TODO 3: Send notification with fluctuation and any relevant articles
# skipping for now

