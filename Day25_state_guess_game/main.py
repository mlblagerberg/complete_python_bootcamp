"""Project: Pandas practice
Start: March 26th, 2024
Last touched: March 26th, 2024
Author: Madeleine L.
"""

with open("weather_data.csv", mode="r") as weather_file:
    weather_data = weather_file.readlines()
    clean_data = []
    for entry in weather_data:
        new_entry = entry.strip()
        clean_data.append(new_entry)


print(clean_data)
