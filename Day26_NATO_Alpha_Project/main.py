"""Project: NATO Alpha Project
Start: April 19th, 2024
Last touched: April 24th, 2024
Author: Madeleine L.
"""

import pandas as pd
# Create a dictionary in this format
# {"A": "Alfa", "B": "Bravo", ... etc}
nato_alpha = pd.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alpha.head())

nato_dict = {row.letter: row.code for (index, row) in nato_alpha.iterrows()}
print(nato_dict)

# Create a list of the phonetic code words from a word that the user inputs.
user_phrase = input("Please input a word or phrase: ").upper()
word_list = user_phrase.split()
for user_word in word_list:
    word_letters = [letter for letter in user_word]
    nato_code = [nato_dict[letter] for letter in word_letters]
    print(f"{user_word}: {nato_code}")
