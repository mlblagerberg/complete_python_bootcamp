"""Project: Stock News Monitor
Start: June 5th 2024
Last touched: June 14th, 2024
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

today = datetime.today().strftime("%Y-%m-%d")
yesterday = (datetime.today() - timedelta(1)).strftime("%Y-%m-%d")
week_ago = (datetime.today() - timedelta(3)).strftime("%Y-%m-%d")

stock_api_key = os.getenv("ALPHA_VANTAGE_API")
# TODO 1: Get stock price delta between current day opening and previous day close
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "ENPH",
    "outputsize": "compact",
    "apikey": stock_api_key,
}

stock_url = "https://www.alphavantage.co/query?"
response = requests.get(stock_url, params=stock_parameters)
stock_data = response.json()
print(stock_data)

today_stock = stock_data["Time Series (Daily)"][today]
yesterday_stock = stock_data["Time Series (Daily)"][yesterday]
#
print(f"Today's stock details: {today_stock}")
# print(f"Yesterday's stock details: {yesterday_stock}")

# TODO 2: If it was a large fluctuation (>10%) then find related news articles for company from the past week
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
print(news_data)

# TODO 3: Send notification with fluctuation and any relevant articles


