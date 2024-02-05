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

# Create dictionary of all cards to keep track of cards used as well as their face value
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

# full_deck = cards

# List of card type and their weights for how often they occur in the deck
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
# Create a list of (suit, card) to capture all possible cards. See below doc string for explanation.
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

## Create function to pull random card and then remove it from the card dictionary
def get_card():
    # Select a random card class, determine the suit and whether the card is a face or low card.
    random_card_class = random.choice(weighted_card_class)
    # Update weighted card class list so that probability of next card is accurate
    weighted_card_class.remove(random_card_class)
    # print(len(weighted_card_class))

    # Card suit is self-explanatory
    card_suit = random_card_class[0]
    # print(card_suit)
    # Card type tells you the face value options of the card
    card_type = random_card_class[1]
    # print(card_type)
    card_type_options = cards[card_suit][card_type]
    # print(card_type_options)
    # Get's the random value of the card
    random_card_value = random.choice(card_type_options)

    if card_type == "A":
        random_card_value = [1, 11]

    # print(f"list of values card could be {card_type_options}")
    # print(f"card suit: {card_suit}")
    # print(f"card type: {card_type}")
    # print(random_card_value)

    # Now we need to remove the card itself from the set of possible cards to play next
    if card_type in ["K", "Q", "J", "A"]:
        del cards[card_suit][card_type]
        # print(f"{card_type} {card_suit} {random_card_value}")
        return [card_type, card_suit, random_card_value]
    else:
        cards[card_suit][card_type].remove(random_card_value)
        # print(f"{random_card_value} {card_suit} {random_card_value}")
        # print("loop")
        return [random_card_value, card_suit, random_card_value]

    # Show user the cards they pulled and the cards the computer pulled
    return                  

# Function to calculate total of dealt hand considering A's possible values of 1 or 11
def hand_total(hand_values):
    int_hand_values = [x for x in hand_values if not isinstance(x, list)]
    if len(int_hand_values) == len(hand_values):
        hand_total = sum(hand_values)
        return hand_total
    else:
        int_total = sum(int_hand_values)
        A_value_lists = [x for x in hand_values if isinstance(x, list)]


        print(f"This should be list of hand values: {hand_values}")

        # print(f"This should be list of integer values in hand: {int_hand_values}")
        print(f"This should be int total: {int_total}")

        # print(f"This should be list of lists if there are any A's in hand{A_value_lists}")
        for i in range(0, len(A_value_lists)):
            # print(f"This should be list of possible As values: {A_value_lists[i]}")
            # print(f"This should be length of i element in A_value_lists {len(A_value_lists[i])}")
            for j in range(0, len(A_value_lists[i]) - 1):
                hand_total_1 = A_value_lists[i][j] + int_total
                # print(f"this should be total with A as 1: {hand_total_1}")
                hand_total_11 = A_value_lists[i][j + 1] + int_total
                # print(f"this should be total with A as 11: {hand_total_11}")
                if max(hand_total_1, hand_total_11) <= 21 and max(hand_total_1, hand_total_11) > 16:
                    return max(hand_total_1, hand_total_11)
                else:
                    return min(hand_total_1, hand_total_11)
            


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play.lower() == "y":
    first_card = get_card()
    computer_first_card = get_card()
    second_card = get_card()
    computer_second_card = get_card()

    user_card_list = [first_card[0], second_card[0]]
    user_card_values = [first_card[2], second_card[2]]
    user_total = hand_total(user_card_values)
    
    comp_card_list = [computer_first_card[0], computer_second_card[0]]
    comp_card_values = [computer_first_card[2], computer_second_card[2]]
    comp_total = hand_total(comp_card_values)

print(f"Your cards are: {user_card_list}")
print(f"Computer's cards for debugging: {comp_card_list}\n")
print(f"Computer's first card: {computer_first_card[0]}")

play = input("Do you want to draw another card? ")
while play.lower() == "y":
    # Pull the next user card and updates lists
    next_card = get_card()
    user_card_list.append(next_card[0])
    user_card_values.append(next_card[2])
    user_total = hand_total(user_card_values)
    if comp_total <= 16:
        next_card = get_card()
        comp_card_list.append(next_card[0])
        comp_card_values.append(next_card[2])
        comp_total = hand_total(comp_card_values) # Update comp total
    print(f"Your cards are: {user_card_list}")
    play = input("Do you want another card? ")

if play == "n":
    comp_play = "y"
    while comp_play == "y":
        if comp_total <= 16:
            next_card = get_card()
            comp_card_list.append(next_card[0])
            comp_card_values.append(next_card[2])
            comp_total = hand_total(comp_card_values) # Update comp total
            print(f"Computer's cards for debugging: {comp_card_list}")
        else:
            comp_play = "n"

print(user_total)
print(comp_total)

if user_total == comp_total:
    print(f"Your cards {user_card_list} and the computers cards {comp_card_list}")
    print("It's a draw!")
elif user_total > 21 and comp_total > 21:
    print(f"Your cards {user_card_list} and the computers cards {comp_card_list}")
    print("It's a draw!")
elif comp_total > 21 and user_total <= 21:
    print(f"Your cards {user_card_list} and the computers cards {comp_card_list}")
    print("You win!")
elif user_total > comp_total and user_total <= 21:
    print(f"Your cards {user_card_list} and the computers cards {comp_card_list}")
    print("You win!")
else:
    print(f"Your cards {user_card_list} and the computers cards {comp_card_list}")
    print("You loose!")

