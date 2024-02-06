"""
Project: Blackjack Capstone
Start: February 5th, 2024
Last touched: February 5th, 2024 
Author: Madeleine L.
"""


### Scope review
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function {enemies}")