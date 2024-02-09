"""
Project: Blackjack Capstone
Start: February 5th, 2024
Last touched: February 7th, 2024 
Author: Madeleine L.
"""

import random
from ascii_logos import ngg_logo
### Scope review
# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")
#     return 

# increase_enemies()
# print(f"enemies outside function {enemies}")

## Local scope - exists within functions. E.g. variables
## Global scope - exists within the module itself, not within a function
# Namespace, the name is only visible within the space it is defined
# There is no block namespace in Python (e.g. variables within conditional statements are defined globally)
# Good practice is to not alter global scope within a function as it can introduce bugs
## Global variables are variables that you do not change later in the script. The standard is to name them
## with all caps, (e.g. PI, URL, etc).

### Number guessing game


# Function to determine if user has won, lost, or can continue playing.
def check_guess(num_guess, lives, rand_num):
    if lives == 0 and num_guess == rand_num:
        print(f"You win! The number was {rand_num}.")
    elif lives == 0 and guess != random_number:
        print(f"You loose. The number was {rand_num}")
    else:
        print(f"You have {lives} attempt(s) to guess the number.")


print(ngg_logo)
print("Welcome to the Number Guessing Game!\nI'm thinging of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1,100)
guess = int(input("Make a guess: "))

# Conditional to assign lives dependening on difficulty selected. Print error handling if not given valid input.
remaining_lives = 0
if difficulty.lower() == "easy":
    remaining_lives = 10
elif difficulty.lower() == "hard":
    remaining_lives = 5
else:
    print(f"{difficulty} is not a valid input. Please try again.")
    exit()

# Loop to check remaining lives before checking accuracy of guess.
while remaining_lives > 0:
    remaining_lives -= 1
    if guess == random_number:
        remaining_lives = 0
    elif guess > random_number:
        print("Too high.")
        guess = int(input("Guess again: "))
    elif guess < random_number:
        print("Too low.")
        guess = int(input("Guess again: "))
    check_guess(guess, remaining_lives, random_number)




