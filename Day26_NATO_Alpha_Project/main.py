"""Project: NATO Alpha Project
Start: April 19th, 2024
Last touched: April 19th, 2024
Author: Madeleine L.
"""

# List Comprehension: new_list = [new_item for item in list]

numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]
print(new_list)

names = ["Alex", "Beth", "Johnny", "Travis", "Steph"]

short_names = [name for name in names if len(name) < 5]
print(short_names)

cap_names = [name.upper() for name in names if len(name) > 5]
print(cap_names)
