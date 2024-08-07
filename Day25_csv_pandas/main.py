"""Project: CSV Practice
Start: March 29th, 2024
Last touched: August 7th, 2024
Author: Madeleine L.
"""

import csv
import pandas as pd

# weather_data_clean = []
# with open("weather_data.csv") as data:
#     weather_data = data.readlines()
#     for entry in weather_data:
#         clean_entry = entry.strip()
#         weather_data_clean.append(clean_entry)
#     print(weather_data_clean)
#
# with open("weather_data.csv") as data:
#     weather_data = csv.reader(data)
#     print(weather_data)
#     temps = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)

# weather_data = pd.read_csv("weather_data.csv")
# print(weather_data["temp"])


def print_csv_rows(file):
    """Takes a single csv file and prints each row."""
    try:
        with open(file, mode='r') as data:
            weather_data = data.readlines()
            for row in weather_data:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file}")


print_csv_rows('weather_data.csv')


def print_csv_dictionary_rows(file):
    """Takes a single csv file and prints each row as a dictionary."""
    try:
        with open(file, mode='r') as data:
            weather_data = csv.DictReader(data)
            for row in weather_data:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file}")


print_csv_dictionary_rows('weather_data.csv')


def print_filtered_csv_rows(file, filter_column, filter_value, filter_function='='):
    """Takes a csv file and three filtering parameters and then prints each row meeting filter requirements as a
    dictionary. filter_column: column name from csv. filter_value: the value you want to filter the column on.
    filter_function: whether you want rows that are equal '=', less '<' than or greater '>' than the filter_value.
    Default is equal."""
    try:
        with open(file, mode='r') as data:
            weather_data = csv.DictReader(data)
            for row in weather_data:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file}")

    if filter_column:



