"""Project: Practice Comprehension
Start: April 23rd, 2024
Last touched: April 23rd, 2024
Author: Madeleine L.
"""

from random import randint
import pandas as pd

# # List Comprehension: new_list = [new_item for item in list (can add if conditional at end)]
#
# numbers = [1, 2, 3]
#
# new_list = [n + 1 for n in numbers]
# print(new_list)
#
# names = ["Alex", "Beth", "Johnny", "Travis", "Steph"]
#
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# cap_names = [name.upper() for name in names if len(name) >= 5]
# print(cap_names)

# Dictionary Comprehension: new_dict = {new_key: new_value for (key,value) in dict.items() (or list) (if) }
names = ["Alex", "Beth", "Johnny", "Travis", "Steph", "Bryan", "Gregory"]

student_scores = {name: randint(0, 100) for name in names}

# print(student_scores)
# print(student_scores["Alex"])
passed_students = {student: grade for (student, grade) in student_scores.items() if grade > 60} #student_scores[student] > 60}

# print(student_scores)
# print(passed_students)

# Iterate over pandas DataFrame
# Simple dictionary
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# # Loop through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# Loop through a dataframe
student_df = pd.DataFrame(student_dict)
for (key, value) in student_df.items():
    print(key)
    # print(value)

# Loop through rows vs columns of a dataframe
for (index, row) in student_df.iterrows():
    # print(index)
    print(row)