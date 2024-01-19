"""
Project: Review randomization and python lists
Start: January 19th, 2024
Last touched: January 19th, 2024 
Author: Madeleine L.
"""
import random

### Randomization in practice
# Python uses Mersenne Twister number generator: https://en.wikipedia.org/wiki/Mersenne_Twister
# Khan Acedemy Overview: https://youtu.be/GtOt7EBNEwQ
# Random walk, picture that chooses next direction based on a random number.

# Middle-squares method. Take a single random number as the seed for your pseudo-random number generator
# Square the seed value and then take the middle value of thre square. This is your next random number.
# This new number becomes your new seed and you repeat the process.

## Trully vs pseudo- random
# Difference between a trully random sequence and a pseudorandom sequence is that a pseudorandom sequence
# will eventually reach see it's initial seed and the sequence will repeat itself. A trully random
# sequence will never repeat. This initial sequence is called the period. The period is strictly limited
# by the length of the initial seed. If you use a a two digit seed, then an algorithm can at most create
# 100 numbers before reusing the initial seed and repeating the cycle. Three digit seed will produce no
# more than 1000 numbers before repeating. Four digits, 10,000 numbers and so on. 

random_int = random.randint(100, 200) # includes values a and b
print(random_int)

random_float = random.random() # Generates random points between 0 and 1, does not include 1  i.e. [0,1)
print(random_float)

# Create random float between 0 and 5
random_test = random.randint(0,5) * random.random() # simpler would be just 5 * random.random()
print(random_test)

### Lists: https://docs.python.org/3/tutorial/datastructures.html 
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut"
#                      , "Massachusetts", "Maryland", "South Carolina", "New Hampshire"
#                      , "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont"
#                      , "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi"
#                      , "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan"
#                      , "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota"
#                      , "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado"
#                      , "North Dakota", "South Dakota", "Montana", "Washington", "Idaho"
#                      , "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # Add item to the end of the list
# states_of_america.append("Puerto Rico")
# print(states_of_america)

# Most pesticide 
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches"
              , "Cheeries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# Creating list of lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cheeries", "Pears", "Tomatoes"]
vegetables = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen2 = [fruits, vegetables]
print(dirty_dozen2)

fruits[-1] = "Melons"
print(fruits)

print(dirty_dozen2[1][1])