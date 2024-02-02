"""
Project: Calculator App
Start: January 31st, 2024
Last touched: February 2nd, 2024 
Author: Madeleine L.
"""

import replit

### Attempt before lesson - build calculator

def calculator(val, op, val2):
    """This function takes three inputs. Two values and one operator. 
    Given those it performs the calculation between the values with 
    the provided operator."""
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
    """This function does not have any inputs.
    It initiates the calculator app and managers the user calls using the 
    calculator function."""
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
        return val
            
# print(calculator(3, "+", 2))
# print(calc_app())

# ## Lesson notes: Functions with outputs
# # Attempt before lesson solution
# def format_name(first_name, last_name):
#     replit.clear() # clearing annoying replit warning...
#     format_names = []
#     name_list = [first_name, last_name]
#     for name in name_list:
#         name = name.lower()
#         name = [*name]
#         name[0] = name[0].upper()
#         name = ''.join(name)
#         format_names.append(name)

#     full_name = print(f"{format_names[0]} {format_names[1]}")
#     return full_name

# # format_name("TesVDEWd", "nweEFme")

# # Lesson uses title case...
# def format_name(f_name, l_name):
#     replit.clear()
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     return f"{formatted_f_name} {formatted_l_name}"

# print(format_name("TesVDEWd", "nweEFme"))


# ### Docstrings - creating documentation for when someone goes to use your function user understands how to use
# #### Leap year code
# # year = input("Please provide a year in the format YYYY. ")
# def is_leap(year):
#     """Takes a year and determines if the year is a leap year or not."""
#     if year % 400 == 0:
#         print("Leap year")
#     elif year % 100 == 0:
#         print("Not leap year")
#     elif year % 4 == 0:
#         print("Leap year")
#     else:
#         print("Not leap year")

# # is_leap(year)

### Lesson solution for calculator
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Dividion by zero."
    else:
        return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calc_app():
    """This function does not have any inputs.
    It initiates the calculator app and managers the user calls using the 
    calculator function."""
    val = int(input("What's the first number? "))
    cont = "y"
    while cont == "y":
        val1 = val
        for op in operations:
            print(op)
        operation_symbol = input("Pick an operation from the list above: ")
        user_operation = operations[operation_symbol]
        val2 = int(input("What's the next number? "))

        result = user_operation(val,val2)
        cont = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        val = result
        replit.clear()
        # calc_app(start)
    if cont.lower() == "n":
        print(f"{val1} {operation_symbol} {val2} = {result}")
        return val
    
calc_app()
