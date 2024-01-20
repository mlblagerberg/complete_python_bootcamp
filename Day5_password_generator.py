"""
Project: Password Generator
Start: January 20th, 2024
Last touched: January 20th, 2024 
Author: Madeleine L.
"""

import random
import string

### Attempt before lesson
print("\nWelcome to the PyPassword Generator!")
pass_length = input("How long do you want your password to be? \n")

# Check for appropriate values
pass_length = int(pass_length)
if pass_length <= 0 or pass_length > 100: # or type(pass_length) != "int":
    print(f"\n{pass_length} is not a valid input, please choose an integer length larger than 0 and smaller than 100.")
else:
    sym_count = input("How many symbols would you like? ")
    sym_count = int(sym_count)
    if sym_count < 0 or sym_count > pass_length:
        print(f"\n{sym_count} would exceed the password length. Please input a symbol count between (0,{pass_length}])\n")
    else:
        num_count = input("How many numbers would you like? ")
        num_count = int(num_count)
        if num_count < 0 or num_count > pass_length - sym_count:
            print(f"\n{num_count} would exceed the password length. Please input a number count between (0,{pass_length - sym_count})\n")
        else:

            # First let's get the random numbers
            num_list = []
            for i in range(0,num_count):
                # update i to be random with each iteration 
                i = str(random.randint(0,9))
                num_list.append(i)

            # print(num_list)
            
            # Now radom symbols
            sym_master = ["@","!","$","%","^","&","*","(",")","<",">"]
            sym_list = []
            for i in range(0,sym_count):
                # update i to be random with each iteration
                i = random.randint(0,9)
                sym_list.append(sym_master[i])
            
            # print(sym_list)

            # create set of all possible letters
            alpha_master = list(string.ascii_lowercase) + list(string.ascii_uppercase)
            # print(alpha_master[40])

            # get random letters
            alpha_list = []
            alpha_length = pass_length - num_count - sym_count
            # Generate password length
            for i in range(0,alpha_length):
                # update i to be random with each iteration
                i = random.randint(0,51)
                # print(i)
                letter = alpha_master[i]
                # print(letter)
                alpha_list.append(letter)
            
            # print(alpha_list)
            
            character_list = num_list + sym_list + alpha_list
                
            # print(character_list)

            # Create random list using the random character list     
            password_list = []       
            j = 0
    
            while len(character_list) > 0:
            
                j = random.randint(0,len(character_list) - 1)
                # print(j)
                password_list.append(character_list[j])
                character_list.remove(character_list[j])
                # print(character_list)
                # print(password_list)

                j += 1

            # create string out of listed characters
            final_password = ''.join(password_list)

# Print final password
print(f"Here is your password: {final_password}\n")
