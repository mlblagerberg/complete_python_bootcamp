"""
Project: Cipher Program
Start: January 26th, 2024
Last touched: January 26th, 2024 
Author: Madeleine L.
"""

import string

# Greet function
def greet():
    print("This is a greet function.")
    print("It is meant to welcome a user to the program.")
    print("Welcome user!")

greet()

### Cipher attempt before lesson
# Get alphabet
alpha_list = list(string.ascii_lowercase)
# print(alpha_list)

# # Create list to store encode/decode indexes
# encode_index = []
# decode_index = []

# # Create list to store encode/decode characters word
# encode_chr = []
# decode_chr = []

# Create function to take any word and any cipher length and return the encoded word
def cipher_encode(word, num):
    # Create list to store encode index and characters of word
    encode_index = []
    encode_chr = []

    word_list = list(word)
    # print(word_list)
    for i in range(0,len(word_list)):
        letter = word_list[i]
 
        # decode_index.append(alpha_list.index(letter))
        # setting encoded index
        ind = (alpha_list.index(letter) + num) % 26
        encode_index.append(ind)
        
        encode_chr.append(alpha_list[encode_index[i]])
        encode_word = ''.join(encode_chr)
    
    print(f"\nYour encoded word is {encode_word}\n")

# cipher_encode("trust",2)

# Create function to take encoded word and cipher length and return decoded word
def cipher_decode(word, num):
    # Create list to store encode index and characters of word
    decode_index = []
    decode_chr = []

    word_list = list(word)
    # print(word_list)
    for i in range(0,len(word_list)):
        letter = word_list[i]
 
        # decode_index.append(alpha_list.index(letter))
        ind = (alpha_list.index(letter) - num) % 26
        decode_index.append(ind)
        
        decode_chr.append(alpha_list[decode_index[i]])
        decode_word = ''.join(decode_chr)
    
    print(f"\nYour decoded word is: {decode_word}\n") 

# cipher_decode("vtwuv",2)


## User calls
# Ask user whether they are encoding or decoding
print("\nWelcome to Ceasar Cipher!")
in_out = input("\nDo you want to encode or decode a word? ")

# Do checks for valid input
if in_out.lower() == "encode":
    in_out = "encode"
elif in_out.lower() == "decode":
    in_out = "decode"
else:
    in_out = input(f"\n{in_out} is not a valid input. Please choose encode or decode. ")

# Ask user for word to encode/decode
word = input(f"\nPlease provide the word you would like {in_out}d. ")

# Ask user for ceasar cipher length
cipher_length = input("\nHow long is your cipher? ")
# print(type(int(cipher_length)))
if type(int(cipher_length)) is False:
    cipher_length = int(input("\nPlease input an integer value for your cipher length."))
# if isinstance(cipher_length, int):
    # cipher_length = input(f"{cipher_length} must be an interger, please provide an input of type int. ")
else:
    cipher_length = int(cipher_length)
    if in_out == "encode":
        cipher_encode(word, cipher_length)
    else:
        cipher_decode(word, cipher_length)
# Call function and give result
