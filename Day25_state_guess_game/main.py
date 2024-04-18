"""Project: Pandas practice
Start: March 26th, 2024
Last touched: April 18th, 2024
Author: Madeleine L.
"""

import csv
import pandas as pd

# with open("weather_data.csv", mode="r") as weather_file:
#     weather_data = weather_file.readlines()
#     clean_data = []
#     for entry in weather_data:
#         new_entry = entry.strip()
#         clean_data.append(new_entry)
#
#
# print(clean_data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data) # this is an object
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)

data = pd.read_csv("weather_data.csv")
# DataFrames are the primary classes/object in pandas
# Every table is a dataframe
# print(type(data))
# Series (like lists) are the other primary classes/object in pandas
# Every column is a series
# print(type(data["temp"]))

# Convert dataframe to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Convert series to list
# temp_list = data["temp"].to_list()
# print(sum(temp_list) / len(temp_list))
# print(data["temp"].mean())
# print(max(temp_list))
# print(data["temp"].max())

# Get particular column
# print(data["condition"])
# Pandas converts each column into attributes e.g. below
# print(data.condition)

# Get data in a row given some constraint
# print(data[data.day == "Wednesday"])
# get row where the temperature was at its maximum
print(data[data.temp == data.temp.max()])

# Get Mondays temp in fehrenheit
monday = data[data.day == "Monday"]
temp_f = (monday.temp * 9/5) + 32
print(temp_f)

# Create dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

df = pd.DataFrame(data_dict)
print(df)
# Save to new csv
df.to_csv("new_data.csv")
# print(data_dict)


