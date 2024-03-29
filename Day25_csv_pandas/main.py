"""Project: CSV Practice
Start: March 29th, 2024
Last touched: March 29th, 2024
Author: Madeleine L.
"""

weather_data_clean = []
with open("weather_data.csv") as data:
    weather_data = data.readlines()
    for entry in weather_data:
        clean_entry = entry.strip()
        weather_data_clean.append(clean_entry)
    print(weather_data_clean)