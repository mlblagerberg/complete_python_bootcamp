"""
Project: OOP Coffee Machine
Start: February 16th, 2024
Last touched: February 16th, 2024
Author: Madeleine L.
"""

import coffee_maker as cm
import money_machine as mm
import menu

# Create object instances from classes
coffee_machine = cm.CoffeeMaker()
money = mm.MoneyMachine()
drink_menu = menu.Menu()

machine_on = True
while machine_on:
    request = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if request == "off":
        print("Goodbye!")
        machine_on = False
        exit()
    elif request == "report":
        # Call report methods from coffee maker and money machine classes
        coffee_machine.report()
        money.report()
    else:










        #
        # # Checks if request is a drink offering
        # drink_menu.find_drink(request)
        # drink_ingredients = drink_menu.menu
        # # print(drink_ingredients[0])
        # check_resources = coffee_machine.is_resource_sufficient(drink_ingredients)
        # # print(f"\n{drink_menu.menu}\n")
        # if money.make_payment(drink_ingredients):
        #     coffee_machine.make_coffee(drink_ingredients)
        #
        #
        #

