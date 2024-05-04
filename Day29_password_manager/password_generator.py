"""Project: Password Generator
Start: May 3rd, 2024
Last touched: May 3rd, 2024
Author: Madeleine L.
"""

import random
import string
# random.seed(100)


class Password:
    def __init__(self, letters_bol, numbers_bol, symbols_bol, pwd_length):
        self.letters = letters_bol
        self.numbers = numbers_bol
        self.symbols = symbols_bol
        self.char_list = [letters_bol, numbers_bol, symbols_bol]
        self.length = pwd_length

    def generate_password(self):
        # Set random count for each character type ensuring count adds up to user specified length and that all
        # character types are included that are specified
        char_lengths = [(random.random() + self.char_list[n]) * self.char_list[n] for n in range(3)]
        total_length = sum(char_lengths)
        char_lengths = [int((m / total_length) * self.length) for m in char_lengths]
        # Logic to add remainder to random character element for only characters user has selected
        non_zero_chars = [n for n in range(len(self.char_list)) if self.char_list[n] != 0]
        char_lengths[random.choice(non_zero_chars)] += self.length - sum(char_lengths)
        # print(char_lengths)

        # letters
        alpha_master = list(string.ascii_lowercase) + list(string.ascii_uppercase)
        alpha_list = [random.choice(alpha_master) for _ in range(char_lengths[0])]
        # numbers
        num_list = [str(random.randint(0, 9)) for _ in range(char_lengths[1])]
        # symbols
        sym_master = ["@", "!", "$", "%", "^", "&", "*", "(", ")", "<", ">"]
        sym_list = [random.choice(sym_master) for _ in range(char_lengths[2])]

        character_list = num_list + sym_list + alpha_list

        # Create random list using the character list
        random.shuffle(character_list)

        # create string out of listed characters
        final_password = ''.join(character_list)
        return final_password
