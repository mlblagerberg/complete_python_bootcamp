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

change = 0
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


# TODO: 4. When user asks for drink check resources before making drink and accepting money. E.g. print "Sorry there is
#  not enough water.
def resource_check(coffee_drink):
    for j in resources:
        if resources[j][0] < MENU[coffee_drink]["ingredients"][j]:
            print(f"Sorry, there is not enough {resources[j][0]}.")
            return False
        else:
            return True


# TODO: 5. If there are enough resources to make the drink, prompt user for coins. Calculate the total inserted
# TODO: 6. Check that user has inserted enough. If not, say "Sorry, that is not enough money. Money refunded." If they
#  have inserted enough add the drink cost to the machine total.
#  If user has given too much money then give change, "Here is $XX.XX change."
def payment():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    total = ((quarters*25) + (dimes*10) + (nickles*5) + pennies) / 100
    return total


# TODO: 7. If enough resources and money, then make the coffee. Update the resources. Tell user here is your XXXX.
#  Enjoy! Print ascii art of coffee product
def make_coffee(coffee_drink):
    '''This function takes a single coffee drink request input, updates resources and outputs a coffee drink'''
    for k in resources:
        resources[k][0] = resources[k][0] - MENU[coffee_drink]["ingredients"][k]
    print(f"\nHere is your {coffee_drink}. Enjoy!")
    print(coffee)

# TODO: 1. Ask user what kind of coffee they want. (espresso/latte/cappuccino).
#  If they enter off, turn machine off. If they enter report, report resources, else proceed with making coffee
#  Report should show values, units and capitalize titles: water: 100ml, milk: 50ml, coffee: 76g, and money: $2.5
coffee_input = input("What would you like? (espresso/latte/cappuccino) ").strip().lower()

if coffee_input == "off":
    print("Goodbye!")
    exit()
elif coffee_input == "report":
    for i in resources:
        print(f"{i.title()}: {resources[i][0]}{resources[i][1]}")
    print(f"Money: ${change}")# water = resources["water"]
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


