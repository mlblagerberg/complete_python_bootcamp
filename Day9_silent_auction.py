"""
Project: Silent Auction
Start: January 30th, 2024
Last touched: January 30th, 2024 
Author: Madeleine L.
"""

### Dictionaries and nestings review
## Dictionaries have two parts a key, and then an associated value or definition of the key.
## Example given is a table with two columns, key and value
## Python syntax is {key: value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    #"Loop": "The action of doing something over and over again.",
                          }

# Retrieve list syntax is list[index]
# Dictionary elements are identified by their key versus index
# print(programming_dictionary["Bug"])

# Dictionary common pitfalls
# 1. Misspelling keys or attempting to retrieve incorrect key
# 2. Data type - key must be provided in actual data type. E.g. key is int 123 so 123 is called not "123"

# Adding new entry to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# Create empty dictionary you can also wipe a dictionary with this as well (useful for restartign games and scores)
empty_dict = {}

# Redefine "Bug" key
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# How to loop through dictionary
for key in programming_dictionary:
    print(key) # returns just the keys
    print(programming_dictionary[key])

# Program to grade a students test score
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# Create an empty dictionary called student_grades then fill it
# 91 - 100: outstanding, 81 - 90: exceeds expectations, 71 - 80: acceptable, <=70: fail
student_grades = {}

for student in student_scores:
    if student_scores[student] > 90:
        student_grades[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_grades[student] = "Exceeds Expectations"
    elif student_scores[student] > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

## Nesting
# {
# key: [List]
# key2: {dict}
# }

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Normandy", "Bayeux"],
    "England": ["London", "Gilford", "Basignstoke"],
}

# Nested lists are not as useful and nest lists in dictionaries or nested dictionaries in dictionaries
# For travel log what if you'd like to store when you visited 
# Create nested dictionary called cities visited
travel_log = {
    "France": {
        "Paris": "2019-12",
        "Normandy": "2020-01",
        "Bayeux": "2020-01"},
    "England": {
        "Lomdon": ["2005-05", "2007-08"],
        "Gilford": "2007-08",
        "Basingstoke": ["2007-08", "2008-10"]
    }
}

for country in travel_log:
    print(travel_log[country])