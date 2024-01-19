"""
Project: Choose your own adventure
Start: January 18th, 2024
Last touched: January 19th, 2024 
Author: Madeleine L.
"""

### Review conditionals
# Rollercoaster Practice: Create a program that asks for a users height and age and responds
# with whether the user can meets the height requirements and how much they need to pay.

# Welcome statement and request user input
print(f"Welcome to the rollercoaster to no where!")
height = int(input(f"We need to check to see if you are tall enough to ride.\nWhat is your height in inches? "))

if height >= 48: # height restriction in inches
    print("You are tall enough to ride!")
    age = int(input("We will now let you know how much your ticket will cost. What is your age? "))
    if age <= 12 or age > 65:
       print("Child and senior tickets are $5.00.")
       total = 5.00
    elif age > 12 and age < 18:
        print("Youth tickets are $7.00.")
        total = 7.00
    else: 
        print("Adult tickets are $12.00.")
        total = 12.00
    picture = input("Would you like to buy a picture of your rollercoaster ride? ")
    if picture == "yes" or picture == "Yes" or picture == "y" or picture == "Y":
        # print(total + 5)
        total += 5
        print(f"That will be an additional $5.00.\n Your total is {total}")
    else:
        print(f'Ok, your total is ${total}')
else:
    print("I am sorry, but you need to be at least 48 inches to ride this roller coaster.")


