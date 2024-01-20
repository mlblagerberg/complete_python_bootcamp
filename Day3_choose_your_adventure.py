"""
Project: Choose your own adventure
Start: January 18th, 2024
Last touched: January 19th, 2024 
Author: Madeleine L.
"""

### Review conditionals
# Rollercoaster Practice: Create a program that asks for a users height and age and responds
# with whether the user can meets the height requirements and how much they need to pay.

# # Welcome statement and request user input
# print(f"Welcome to the rollercoaster to no where!")
# height = int(input(f"We need to check to see if you are tall enough to ride.\nWhat is your height in inches? "))

# # check height to determine ride eligibility
# if height >= 48: # height restriction in inches
#     print("You are tall enough to ride!")

#     # check age to determine ticket price
#     age = int(input("We will now let you know how much your ticket will cost. What is your age? "))
#     if age <= 12 or age > 65:
#        print("Child and senior tickets are $5.00.")
#        total = 5.00
#     elif age > 12 and age < 18:
#         print("Youth tickets are $7.00.")
#         total = 7.00
#     elif age >= 45 and age <= 55:
#         print("Your ticket is free!")
#         total = 0
#     else: 
#         print("Adult tickets are $12.00.")
#         total = 12.00
    
#     # if their height meets the height requirements ask if they want to purchase a picture
#     picture = input("Would you like to buy a picture of your rollercoaster ride? ")

#     if picture == "yes" or picture == "Yes" or picture == "y" or picture == "Y":
#         # print(total + 5)
#         total += 5
#         print(f"That will be an additional $5.00.\nYour total is {total}")
#     else:
#         print(f'Ok, your total is ${total}')
# else:
#     print("I am sorry, but you need to be at least 48 inches to ride this roller coaster.")

### Treasure Island Project
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

step1 = input('''
    You wake up and get the urge to go for a walk.
    You've wandered into a wooded area that you've never seen before.
    To your left you can hear the ocean, to your right you see a light beyond some trees.
    Which way do you go? 
    
    ''')

if step1.lower() == "left":
    step2 = input(f'''
    You've decided to go {step1.lower()} and find yourself on a cliff looking out at the see.
    In the distance you see someone in the water, you call 911.
    Do you wait for help to arrive or swim out to help them? 
    
    ''')

    if "swim" in step2.lower().split():
        print(f"\n    You chose to swim and were sucked out to sea in a current. Game Over!\n")
    else:
        step3 = input('''
    You chose to wait which either means your a coward or smart... 
    either way, you see that behind a large boulder are three small doors.
    One red, one blue and one yellow. You decide you need to check them out 
    to see if there is a life raft or any floatation device to throw to the 
    person in the water.
    
    Which door do you choose?

    ''')
        if "yellow" in step3.lower().split():
            print('''
    Maybe it was your yellow belly that made you choose this door,
    or maybe it was your internal guilt for not immediately jumping in
    the water... or maybe it was because yellow is like the sun and it
    reminded you of light and all that is good in the world. 
    
    Whatever the reason, you choose correct! Behind the yellow door are 
    stairs which lead to a boat which lets you save the person in the 
    water, who happens to be a billionaire and rewards you handsomely!
                  
    You win!
    
                   $$ $$
                   $$ $$
                  $$$ $$$
               $$$$$$ $$$$$$
             $$$$$$$$ $$$$$$$$        
            $$$$$  $$ $$ $$$$$$
           $$$$    $$ $$  $$$$$$
           $$$$    $$ $$  $$$$$$
            $$$$$  $$ $$          
             $$$$$ $$ $$     
               $$$$$$ $$
                 $$$$ $$$$
                  $$$ $$$$$
                   $$ $$$$$$$
                   $$ $$ $$$$
                   $$ $$  $$$$$
                   $$ $$   $$$$$
           $$$$$$  $$ $$    $$$$
           $$$$$$  $$ $$   $$$$$
            $$$$$$ $$ $$  $$$$$
              $$$$$$$ $$$$$$$$
                $$$$$ $$$$$$
                  $$$ $$$
                   $$ $$
                   $$ $$

    ''')
        elif "red" in step3.lower().split():
            print('''
    Well that was a mistake, behind the red door is a man eating lion.
    You are now its snack. Game over!
            
    ''')
        elif "blue" in step3.lower().split():
            print('''
    Blue, the color of sorrow... You find a room of corpses and are over
    taken by the stench. You pass out and are found by the emergency 
    responders you'd called. Unfortunately, they cannot find the person you
    claimed was in the water and it is beginning to look like you may
    be a serial killer. Tough luck! Game over!
            
    ''')
        else:
            print("Well you have to choose a door, so sense you didn't, you are\nnow in an infinite void.\n Game over!\n")
else:
    print(f"\n    You've followed the light to the {step1.lower()}, and get hypnotized by a witch. Game over!")
    