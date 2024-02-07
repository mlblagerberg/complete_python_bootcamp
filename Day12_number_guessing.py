"""
Project: Blackjack Capstone
Start: February 5th, 2024
Last touched: February 5th, 2024 
Author: Madeleine L.
"""

import random
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
def check_guess(num_guess, lives, rand_num):
    if lives == 0 and num_guess == rand_num:
        print(f"You win! The number was {rand_num}.")
    elif remaining_lives == 0 and guess != random_number:
        print(f"You loose. The number was {rand_num}")
    else:
        print(f"You have {lives} attempt(s) to guess the number.")

print("Welcome to the Number Guessing Game!\nI'm thinging of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number = random.randint(1,100)
guess = int(input("Make a guess: "))

# print([*difficulty])
if difficulty.lower() == "easy":
    remaining_lives = 10
elif difficulty.lower == "hard":
    remaining_lives = 5
else:
    remaining_lives = 5
# print(remaining_lives)

while remaining_lives > 0:
    remaining_lives -= 1
    if guess == random_number:
        print("You win!")
        remaining_lives = 0
    elif guess > random_number:
        print("Too high.")
        # print(f"You have {remaining_lives} attempt(s) to guess the number.")
        guess = int(input("Guess again: "))
    elif guess < random_number:
        print("Too low.")
        # print(f"You have {remaining_lives} attempt(s) to guess the number.")
        guess = int(input("Guess again: "))
    check_guess(guess, remaining_lives, random_number)

    

# If hard then you have 5 attempts to guess (print this out)
# If easy you have 10 attempts  
# Ask for initial guess then tell the user if they are too high or too low and then reduce their remaining number of guesses.
# Repeat until user guesser or is out of turns.




