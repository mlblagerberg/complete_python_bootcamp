"""
Project: Coffee Machine
Start: February 9th, 2024
Last touched: February 9th, 2024 
Author: Madeleine L.
"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
}

coffee = '''
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|+++++++++| 
 `-'_________'
    '-------'
'''


def resource_check(coffee_drink):
    """This functions takes a coffee drink input espresso/latte/cappuccino and outputs boolean for whether the coffee
    machine has enough resources to make the drink."""
    for j in resources:
        if resources[j][0] < MENU[coffee_drink]["ingredients"][j]:
            print(f"Sorry, there is not enough {resources[j][0]}.")
            return False
        else:
            return True


def update_resources(coffee_drink):
    """Takes a coffee drink espresso/latte/cappuccino as input and returns the available resources and money that the
    coffee machine currently has"""
    global resources, money
    for k in resources:
        resources[k][0] -= MENU[coffee_drink]["ingredients"][k]
    money += MENU[coffee_drink]["cost"]
    return resources, money


def payment():
    """This function has no inputs but initiates the user calls to insert payment in coins for the coffee drink they've
    selected. It returns the total amount the user has inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = ((quarters*25) + (dimes*10) + (nickles*5) + pennies) / 100
    return total


def make_coffee(coffee_drink):
    """This function takes a single coffee drink request input, updates resources and outputs a coffee drink"""
    update_resources(coffee_drink)
    print(f"\nHere is your {coffee_drink}. Enjoy!")
    print(coffee)


def coffee_maker():
    """This function initiates the coffee maker program. It is recursive and will continue to run until the user
    responds off. The options are to select a coffee to make, espresso/latte/cappuccino, ask for a report, or turn off.
    """
    coffee_input = input("What would you like? (espresso/latte/cappuccino) ").strip().lower()

    if coffee_input == "off":
        print("Goodbye!")
        exit()
    elif coffee_input == "report":
        for i in resources:
            print(f"{i.title()}: {resources[i][0]}{resources[i][1]}")
        print(f"Money: ${money}")
    elif coffee_input in ["espresso", "latte", "cappuccino"]:
        if resource_check(coffee_drink=coffee_input):
            total = payment()
            if total == MENU[coffee_input]["cost"]:
                make_coffee(coffee_drink=coffee_input)
            elif total < MENU[coffee_input]["cost"]:
                print(f"\nSorry, that is not enough money. ${total} refunded.")
            else:
                change = round(total - MENU[coffee_input]["cost"], 2)
                print(f"Your change is ${change}.")
                make_coffee(coffee_drink=coffee_input)
    coffee_maker()


coffee_maker()


