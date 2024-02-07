"""
Project: Blackjack Capstone
Start: February 5th, 2024
Last touched: February 5th, 2024 
Author: Madeleine L.
"""


### Scope review
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    return 

increase_enemies()
print(f"enemies outside function {enemies}")

## Local scope - exists within functions. E.g. variables
## Global scope - exists within the module itself, not within a function
# Namespace, the name is only visible within the space it is defined
# There is no block namespace in Python (e.g. variables within conditional statements are defined globally)
# Good practice is to not alter global scope within a function as it can introduce bugs
## Global variables are variables that you do not change later in the script. The standard is to name them
## with all caps, (e.g. PI, URL, etc).

### Number game
print("Welcome to the Number Guessing Game!\nI'm thinging of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard.")
# If hard then you have 5 attempts to guess (print this out)
# If easy you have 10 attempts
# Ask for initial guess then tell the user if they are too high or too low and then reduce their remaining number of guesses.
# Repeat until user guesser or is out of turns.


