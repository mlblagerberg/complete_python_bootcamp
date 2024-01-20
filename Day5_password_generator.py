"""
Project: Password Generator
Start: January 20th, 2024
Last touched: January 20th, 2024 
Author: Madeleine L.
"""

import random
import string

### Attempt before lesson
print("Welcome to the PyPassword Generator!")
pass_length = input("How long do you want your password to be? ")

# Check for appropriate values
pass_length = int(pass_length)
if pass_length <= 0 or pass_length > 100: # or type(pass_length) != "int":
    print(f"\n{pass_length} is not a valid input, please choose an integer length larger than 0 and smaller than 100.")
else:
    sym_count = input("How many symbols would you like? ")
    sym_count = int(sym_count)
    if sym_count < 0 or sym_count > pass_length:
        print(f"\n{sym_count} would exceed the password length. Please input a symbol count between (0,{pass_length}])")
    else:
        num_count = input("How many numbers would you like? ")
        num_count = int(num_count)
        if num_count < 0 or num_count > pass_length - sym_count:
            print(f"\n{num_count} would exceed the password length. Please input a number count between (0,{pass_length - sym_count})")
        else:

            for i in range(1,num_count):
                


            alpha_list = list(string.ascii_lowercase) + list(string.ascii_uppercase)
            # print(alpha_list)

            # Generate password length
            for i in range(0,pass_length):
                password_list.append(i)
            

                
            # print(password_list)



