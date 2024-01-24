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

print(f'''
Welcome to the hangman game! 
      
{hangman_images.get_image(0)}

Word to guess: {word_spaces_str}
''')


# Define function to ask the user to guess a letter
def user_guess():
    letter_guess = input("\n>>> Guess a letter: ")
    return(letter_guess)

# Set empty list to keep track of the letters the user has guessed so far
guessed_letters = []
no_match_letters = []
failed_attempts = 0

# Loop to play game while user still has attempts left
while failed_attempts < 10 and word_spaces.count("_ ") > 0:

    # get user input letter
    letter = user_guess().lower()
    # tests to ensure that the input was a letter
    if letter in guessed_letters:
        print("You've already guessed that letter. Please guess again.")
    elif letter not in alpha_list:
        print(f"{letter} is not a valid input. Please guess again.")
    else:
        # check if letter is in the word and if so how many instances
        if letter in word_list:
            count_letter = word_list.count(letter)
            # loop over letter instance count, place in word blanks shown to user, and remove from word list
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
            # keep track of the letters that have been guessed so we can tell user when they have duplicate inputs
            guessed_letters.append(letter)

            #print image of hangman status
            print(hangman_images.get_image(failed_attempts))

            # show user updated word including correct letters guessed
            print(word_spaces_str)
            # print letters guessed that were incorrect
            print(f"\nLetters guessed so far: {no_match_letters}\n")

            # check if there are any letters left to guess in word, if not, then tell user they won
            if word_spaces.count("_ ") == 0:
                print(f"The word is {word_spaces_str.upper()}\nYou win!!!")

        # If user guesses letter not in word, increase failed attempts by one and choose failure type
        else:
            failed_attempts += 1
            # Check if that was the last allowed failed attempt and if so print hangman and let user know they lost
            if failed_attempts == 10:
                print(hangman_images.get_image(failed_attempts))
                print(f"{word_spaces_str}")
                print(f"\nLetters guessed so far: {no_match_letters}\n")
                print("\nYou lost!")
            # If user has more attempts print updated hangman, word, and list of letters guessed. Update letters guessed and no match list.
            else:
                print(hangman_images.get_image(failed_attempts))

                print(f"{word_spaces_str}")

                guessed_letters.append(letter)
                no_match_letters.append(letter)
                
                print(f"\nLetters guessed so far: {no_match_letters}\n")







