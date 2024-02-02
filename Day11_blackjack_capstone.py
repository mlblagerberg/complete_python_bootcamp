"""
Project: Blackjack Capstone
Start: February 2nd, 2024
Last touched: February 2nd, 2024 
Author: Madeleine L.
"""

import random

# Do you want to play a game of Blackjack? Type 'y' or 'n':
# y initiates game and shows ascii art. It gives you two cards in a list format and then the "Computer's first card:" 
# Type 'y' to get another card, type 'n' to pass:
# with 'n' shows your final hand and the computers final hand as lists. then who won and asks if you want to play again or not

### Attempt before lesson 
cards = {
    "clubs": {
    "J": [10],
    "Q": [10],
    "K": [10],
    "A": [1, 11],
    "low": [2,3,4,5,6,7,8,9,10]
    },
    "diamonds": {
    "J": [10],
    "Q": [10],
    "K": [10],
    "A": [1, 11],
    "low": [2,3,4,5,6,7,8,9,10]
    },
    "spades": {
    "J": [10],
    "Q": [10],
    "K": [10],
    "A": [1, 11],
    "low": [2,3,4,5,6,7,8,9,10]
    },
    "hearts": {
    "J": [10],
    "Q": [10],
    "K": [10],
    "A": [1, 11],
    "low": [2,3,4,5,6,7,8,9,10],
    },
}

card_weights = {
    "clubs": {
    "J": 1,
    "Q": 1,
    "K": 1,
    "A": 2,
    "low": 9,
    },
    "diamonds": {
    "J": 1,
    "Q": 1,
    "K": 1,
    "A": 2,
    "low": 9,
    },
    "spades": {
    "J": 1,
    "Q": 1,
    "K": 1,
    "A": 2,
    "low": 9,
    },
    "hearts": {
    "J": 1,
    "Q": 1,
    "K": 1,
    "A": 2,
    "low": 9,
    },
}

# print(card_weights.items())

weighted_card_class = [(suit, card) 
                 for suit, card_options in card_weights.items() 
                    for card, weight in card_options.items() 
                        for _ in range(weight)]
"""Inside the inner loop, we have a third loop that repeats the card a number of 
times equal to its weight. The variable _ is used as a convention in Python when 
you don't intend to use the loop variable; in this case, it's used to indicate 
that we want to repeat the card name based on its weight.
"""
# print(weighted_card_class)
# print(len(weighted_list)) # check to make sure we have the number of cards we expect to have should be 52 + 4 since A's have two possible values.

suit_options = ["clubs", "diamonds", "spades", "hearts"]

random_card_class = random.choice(weighted_card_class)
print(random_card_class)

card_suit = cards[random_card_class[0]]
card_type = cards[random_card_class[0]][random_card_class[1]]


random_card_value = random.choice(card_type)


# print(card_suit)
# print(card_type)
print(random_card_value)

