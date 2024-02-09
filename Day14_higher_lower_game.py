"""
Project: Higher or Lower Game
Start: February 9th, 2024
Last touched: February 9th, 2024 
Author: Madeleine L.
"""

from random import randint
from replit import clear
from high_low_game_data import high_low_data
import ascii_logos


def get_entry(data=high_low_data):
    '''Takes a list of dictionaries with specific item names and outputs dictionary elements for a random list item. Returns list of dictionary element items.'''
    rand_value = randint(0,len(data)-1)
    rand_entry = data[rand_value]
    entry_name = rand_entry['name']
    entry_score = rand_entry['follower_count']
    entry_description = rand_entry['description']
    entry_country = rand_entry['country']
    return [entry_name, entry_score, entry_description, entry_country]


def check_guess(guess, followers_A, followers_B):
    '''Checks if A has more followers than B and if so returns whether or not the 
    guess was A as boolean else returns whether or not guess was B as boolean.'''
    if followers_A > followers_B:
        return guess == "A"
    else:
        return guess == "B"



compare_A = []
compare_B = []
play = True
score = 0
while play:
    clear()
    print(ascii_logos.high_low_logo)
    # Check if we are just starting the game or if we have been playing if we are 
    # just starting get a new entry for A, else replace A with B.
    if len(compare_A) == 0:
        compare_A = get_entry()
    else:
        compare_A = compare_B
        print(f"You're right! Current score: {score}")
    
    print(f"Compare A: {compare_A[0]}, {compare_A[2]}, from {compare_A[3]}")
    print(ascii_logos.vs_logo2)
    compare_B = get_entry()
    if compare_A == compare_B:
        compare_B = get_entry()
    print(f"Against B: {compare_B[0]}, {compare_B[2]}, from {compare_B[3]}")
    
    user_guess = input("Who has more followers? Type 'A' or 'B': ")

    if check_guess(guess=user_guess, followers_A=compare_A[1], followers_B=compare_B[1]):
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        clear()
        play = False
        print(f"Sorry, that's wrong. Final score: {score}")





