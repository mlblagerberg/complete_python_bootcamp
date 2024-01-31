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
    format_names = []
    name_list = [first_name, last_name]
    for name in name_list:
        name = name.lower()
        name = [*name]
        name[0] = name[0].upper()
        name = ''.join(name)
        format_names.append(name)

    full_name = print(f"{format_names[0]} {format_names[1]}")
    return full_name

# format_name("TesVDEWd", "nweEFme")

# Lesson uses title case...
def format_name(f_name, l_name):
    replit.clear()
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("TesVDEWd", "nweEFme"))
