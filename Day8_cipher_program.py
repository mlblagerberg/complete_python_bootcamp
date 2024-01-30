"""
Project: Cipher Program
Start: January 26th, 2024
Last touched: January 29th, 2024 
Author: Madeleine L.
"""

import string
import math
from caesar_cipher_image import logo

### Final Caesar Cipher function
# Get alphabet
alpha_list = list(string.ascii_lowercase)
# print(alpha_list)

## Create single function that can either encode or decode

# Create function to take encoded word and cipher length and return decoded word
def caesar(word, num, direction):
    # Create lists to store new characters of input word and keep track of non-alpha chatacters in statements.
    caesar_chr = []
    non_alpha_index = []
    non_alpha_chr = []
    # Conver input word/statement into list to itterate over.
    word_list = list(word.lower())
    # Assign input type as word as default
    input_type = "word"
    # Check for valid direction inputs and raise error if no valid input was given
    if direction.lower() not in ["encode", "decode"]:
        print(f"{direction} is not a valid input for direction. Please choose encode or decode.")
    else:
        # Check if this is a decode call and change sign of number to subract cipher length
        if direction.lower() == "decode":
            num *= -1
        # Loop over list characters in word/statement and 
        for i in range(0,len(word_list)):
            chr = word_list[i]
            if chr not in alpha_list:
                non_alpha_index.append(int(word_list.index(chr)))
                non_alpha_chr.append(chr)
                word_list[int(word_list.index(chr))] = "X"
                input_type = "statement"
            else:
                # setting index for alpha characters
                ind = (alpha_list.index(chr) + num) % 26
                caesar_chr.append(alpha_list[ind])

        for i in range(0,len(non_alpha_chr)):
            caesar_chr.insert(non_alpha_index[i], non_alpha_chr[i])

        caesar_word = ''.join(caesar_chr)
        print(f"\nYour {direction}d {input_type} is: {caesar_word}\n")
        

## User call
# Ask user whether they are encoding or decoding
def caesar_user_call(rerun=False):
    #Check for rerun status 
    if rerun is False:
        print("\nWelcome to Ceasar Cipher!")
        print(logo)
    in_out = input("\nDo you want to encode or decode a word? ")

    # Ask user for word to encode/decode
    word_in = input(f"\nPlease provide the word or statement you would like {in_out}d. ")

    # Ask user for cipher length
    cipher_length = input("\nHow long is your cipher? ")
    cipher_length = int(cipher_length)

    caesar(word=word_in,num=cipher_length,direction=in_out)

    rerun = input(f"\nWould you like to run the program again? ")
    if rerun.lower() == "yes":
        caesar_user_call(rerun=True)
    else:
        print("Goodbye!\n")

caesar_user_call()

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
