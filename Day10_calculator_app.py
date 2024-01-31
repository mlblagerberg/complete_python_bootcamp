"""
Project: Calculator App
Start: January 31st, 2024
Last touched: January 31st, 2024 
Author: Madeleine L.
"""

import replit

### Attempt before lesson

def calculator(val, op, val2):
    if op in ["+", "-"]:
        if op == "-":
            val2 *= -1
        calc = val + val2
        return calc
    elif op in ["*", "/"]:
        if op == "/":
            if val2 != 0:
                val2 = (1/val2)
            else:
                print("Error: division by zero. Please try again.")
        calc = val * val2
        return calc
    else:
        print(f"{op} is not a valid operator. Please choose from the provided list.")

def calc_app():
    val = float(input("What's the first number? "))
    cont = "y"
    while cont == "y":
        op = input(f"+\n-\n*\n/\nPick an operation: ")
        val2 = float(input("What's the next number? "))
        result = calculator(val, op, val2)
        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        val = result
        replit.clear()
        # calc_app(start)
    if cont.lower() == "n":
        return calc
            
# print(calculator(3, "+", 2))
# print(calc_app())

## Lesson notes: Functions with outputs
def format_name(first_name, last_name):
    replit.clear() # clearing annoying replit warning...
    first_name = [*first_name]
    first_name[0] = first_name[0].upper()
    first_name = ''.join(first_name)
    last_name = [*last_name]
    last_name[0] = last_name[0].upper()
    last_name = ''.join(last_name)

    full_name = print(f"{first_name} {last_name}")
    return full_name

format_name("test", "name")

