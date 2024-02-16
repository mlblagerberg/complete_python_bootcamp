"""
Project: OOP Coffee Machine
Start: February 16th, 2024
Last touched: February 16th, 2024
Author: Madeleine L.
"""

import coffee_maker as cm
import money_machine as mm
import menu


coffee_input = input("What would you like? (espresso/latte/cappuccino) ").lower()

# Create object instances from classes
coffee_machine = cm.CoffeeMaker()
money = mm.MoneyMachine()
# menu_items = menu.MenuItem()
drink_menu = menu.Menu()

if coffee_input == "off":
    print("Goodbye!")
    exit()
elif coffee_input == "report":
    # Call report methods from coffee maker and money machine classes
    coffee_machine.report()
    money.report()
else:

