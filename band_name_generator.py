"""
Project: Band Name Generator
Start: January 17th, 2024
Last touched: January 17th, 2024 
Author: Madeleine L.
"""

### Program output
# Welcome to the Band Name Generator.
# What's the name of the city you grew up in?
# What's your pet's name?

print('Hello World!')
print('Hello, ' + 'You suck... ' + '...JK.')

# Basic interactions with user
user_name = input("\nOk, really. What is your name? ")
print(f"Hello, {user_name}")

# Calculate the length of a tring input
# print(len(input()))

# Reference user_name above rather than asking for input twice
print(f'Your name has {len(user_name)} letters in it!')

### Band name generator

user_hometown = input('\nWhat is the name of your hometown? ')
pet_name = input('\nWhat is the name of your current pet? ')
print(f'Alright, {user_name}. Your bandname is... {user_hometown} {pet_name}!')
