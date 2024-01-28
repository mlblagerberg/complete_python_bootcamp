"""
Project: Cipher Program
Start: January 26th, 2024
Last touched: January 28th, 2024 
Author: Madeleine L.
"""

import string
import math
# import operator

# Greet function
# def greet():
#     print("This is a greet function.")
#     print("It is meant to welcome a user to the program.")
#     print("Welcome user!")

# greet()

### Cipher attempt before lesson
# Get alphabet
alpha_list = list(string.ascii_lowercase)
# print(alpha_list)

## Create single function that can either encode or decode

# Create function to take encoded word and cipher length and return decoded word
def caeser(word, num, direction):
    # Create list to store new characters of input word
    caeser_chr = []
    word_list = list(word)
    if direction.lower() not in ["encode", "decode"]:
        print(f"{direction} is not a valid input for direction. Please choose encode or decode.")
    else:
        if direction.lower() == "decode":
            num *= -1
        for i in range(0,len(word_list)):
            letter = word_list[i]
            # setting index
            ind = (alpha_list.index(letter) + num) % 26
            caeser_chr.append(alpha_list[ind])
            caeser_word = ''.join(caeser_chr)
        print(f"\nYour {direction}d word is: {caeser_word}\n") 

## User call
# Ask user whether they are encoding or decoding
print("\nWelcome to Ceasar Cipher!")
in_out = input("\nDo you want to encode or decode a word? ")

# Ask user for word to encode/decode
word_in = input(f"\nPlease provide the word you would like {in_out}d. ")

# Ask user for cipher length
cipher_length = input("\nHow long is your cipher? ")
cipher_length = int(cipher_length)

caeser(word=word_in,num=cipher_length,direction=in_out)

### Lesson notes
# print(math.ceil(7.3))

## Prime number checker | Lesson solution much cleaner than mine
def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

# prime_checker(10)
