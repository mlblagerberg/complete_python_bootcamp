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
# print(ascii_logos.vs_logo2)
# data format
    # {
    #     'name': 'Instagram',
    #     'follower_count': 346,
    #     'description': 'Social media platform',
    #     'country': 'United States'
    # },

def get_entry(data=high_low_data):
    rand_value = randint(0,len(data)-1)
    rand_entry = data[rand_value]
    entry_name = rand_entry['name']
    entry_score = rand_entry['follower_count']
    entry_description = rand_entry['description']
    entry_country = rand_entry['country']
    return [entry_name, entry_score, entry_description, entry_country]
    # entry_index = 


compare_A = []
compare_B = []
play = True
score = 0
while play:
    clear()
    if len(compare_A) == 0:
        print(ascii_logos.high_low_logo)
        compare_A = get_entry()
    else:
        compare_A = compare_B
    
    print(f"Compare A: {compare_A[0]}, {compare_A[2]}, from {compare_A[3]}")
    print(ascii_logos.vs_logo2)
    compare_B = get_entry()
    print(f"Against B: {compare_B[0]}, {compare_B[2]}, from {compare_B[3]}")
    
    user_guess = input("Who has more followers? Type 'A' or 'B' ")

    if user_guess == 'A' and compare_A[1] >= compare_B[1]:
        score += 1
    elif user_guess == 'A' and compare_A[1] < compare_B[1]:
        play = False
        print(f"Sorry, that's wrong. Final score: {score}")
    elif user_guess == 'B' and compare_B[1] >= compare_A[1]:
        score += 1
    else:
        play = False
        print(f"Sorry, that's wrong. Final score: {score}")






