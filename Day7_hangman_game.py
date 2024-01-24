"""
Project: Hangman Game Program
Start: January 23th, 2024
Last touched: January 24th, 2024 
Author: Madeleine L.
"""

import random
import string
import hangman_images


### Hangman attempt before lesson
alpha_list = list(string.ascii_lowercase)

words = ["bright", "splash", "sunshine", "funny", "mimosa", "victory"]
word = random.choice(words).lower()

# print([*word]) # asterisk before string "unpacks" the letters of word into a list

word_list = [*word]

# Create list of ___ to show user length of word
word_spaces = []
for i in range(0, len(word_list)):
    word_spaces.append("_ ")

# Convert to string to print properly
word_spaces_str = ''.join(word_spaces)

# Set the number of turns 
# turns = 11


# Initiate user interaction and ask for first guess
print(f'''Welcome to the hangman game! 
      
      
Word to guess: {word_spaces_str}
      
''')

# Define function to ask the user to guess a letter
def user_guess():
    letter_guess = input("\nGuess a letter: ")
    return(letter_guess)

# Set empty list to keep track of the letters the user has guessed so far
guessed_letters = []
failed_attempts = 0
# print(word_spaces)

while failed_attempts <= 11 and word_spaces.count("_ ") > 0:
    letter = user_guess()
    print(letter)
    if letter in guessed_letters:
        print("You've already guessed that letter. Please guess again.")
    elif letter not in alpha_list:
        print(f"{letter} is not a valid input. Please guess again.")
    else:
        if letter in word_list:
            count_letter = word_list.count(letter)
            while count_letter > 0:
                
                # get the index of the first instance
                index = word_list.index(letter)
                
                # replace correct empty space with letter
                word_spaces[index] = letter
                
                # update string
                word_spaces_str = ''.join(word_spaces)
                
                # remove letter from word 
                word_list[index] = 0

                # Update count of instances 
                count_letter -= 1
            
            print(word_spaces_str)
            # turns -= 1
            
            guessed_letters.append(letter)

            print(hangman_images.get_image(failed_attempts))

            if word_spaces.count("_ ") == 0:
                print(f"\nThe word is {word_spaces_str}\nYou win!!!")
        
        else:
            print(f"{letter} is not in the word. Try again.")
            guessed_letters.append(letter)
            print(f"Letters guessed so far: {guessed_letters}\n")
            # turns -= 1
            failed_attempts += 1
            print(hangman_images.get_image(failed_attempts - 1))
            if failed_attempts == 11:
                print("\nYou lost!")



    # for i in range(0,len(word_list)):
    # letter_guess = input(f"Please guess a letter: ")

# guessed_letters = guessed_letters.append(letter_guess)





