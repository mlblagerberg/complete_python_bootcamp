"""
Project: Tip Calculator 
Start: January 18th, 2024
Last touched: January 18th, 2024 
Author: Madeleine L.
"""

# if __name__ == "__main__":
#     split_bill(150,4,10)



### Tip Calculator

# Define function to calculate total with tip
def split_bill(pretax_total, count_people, tip_percent):
    
    # Convert inputs into floats for calculations.
    pretax_total = float(pretax_total)
    count_people = int(count_people)
    tip_percent = float(tip_percent)

    # Ensure valid inputs were received before going to calculations
    if pretax_total <= 0:
        print(f'{pretax_total} is not a valid bill amount. Please enter a total amount greater than 0.')
    elif count_people <= 0:
        print(f'{count_people} is not a valid number of people. Please enter a value of 1 or greater.')
    elif tip_percent < 0:
        print(f'{tip_percent} is not a valid tip amount. Please enter a percentage greater or equal to 0.')
    else:
        # Calculate total with tip
        total_amount = pretax_total + (pretax_total * (tip_percent / 100))

        # Calculate per person total
        per_person_amount = total_amount / count_people
        # return per_person_amount

        # Return the value each person needs to pay
        print(f'The amount each person should pay is {per_person_amount}')


# Program to create user facing calls
# Print welcome message and ask for total bill amount
pretax_total = input('Welcome to the tip calculator.\nWhat was the total bill amount? ')

# Ask how many people are splitting the bill
count_people = input('How many people are splitting the bill? ')

# Ask what percent tip they want to give
tip_percent = input('What percentage tip would you like to give? ')


split_bill(pretax_total, count_people, tip_percent)


# # Return the value each person needs to pay
# print(f'The amount each person should pay is {per_person_amount}')

