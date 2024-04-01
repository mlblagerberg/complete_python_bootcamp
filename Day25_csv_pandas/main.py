"""Project: CSV Practice
Start: March 29th, 2024
Last touched: March 29th, 2024
Author: Madeleine L.
"""

import csv
import pandas as pd

weather_data_clean = []
with open("weather_data.csv") as data:
    weather_data = data.readlines()
    for entry in weather_data:
        clean_entry = entry.strip()
        weather_data_clean.append(clean_entry)
    print(weather_data_clean)

with open("weather_data.csv") as data:
    weather_data = csv.reader(data)
    print(weather_data)
    temps = []
    for row in weather_data:
        if row[1] != "temp":
            temps.append(int(row[1]))
    print(temps)

weather_data = pd.read_csv("weather_data.csv")
print(weather_data)
