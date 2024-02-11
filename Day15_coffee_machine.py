"""
Project: Coffee Machine
Start: February 9th, 2024
Last touched: February 9th, 2024 
Author: Madeleine L.
"""

# TODO: 1. Ask user what kind of coffee they want. (espresso/latte/cappuccino).
coffee_input = input("What would you like? (espresso/latte/cappuccino)").lower()

if coffee_input == "off":
    print("Goodbye!")
    exit()
elif coffee_input == "report":
    print("report")
# TODO: 3. When user enters prompt for report, generate report that shows current resource values: water: 100ml, milk:
#  50ml, coffee: 76g, and money: $2.5
# TODO: 4. When user asks for drink check resources before making drink and accepting money. E.g. print "Sorry there is
#  not enough water."
# TODO: 5. If there are enough resources to make the drink, prompt user for coins. Calculate the total inserted
# TODO: 6. Check that user has inserted enough. If not, say "Sorry, that is not enough money. Money refunded." If they
#  have inserted enough add the drink cost to the machine total.
#  If user has given too much money then give change, "Here is $XX.XX change."
# TODO: 7. If enough resources and money, then make the coffee. Update the resources. Tell user here is your XXXX.
#  Enjoy! Print ascii art of coffee product

