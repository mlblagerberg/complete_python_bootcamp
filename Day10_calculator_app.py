"""
Project: Calculator App
Start: January 31st, 2024
Last touched: January 31st, 2024 
Author: Madeleine L.
"""

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

def calc_app(start = 0):
    if start == 0:
        val = int(input("What's the first number? "))

    op = input(f"+\n-\n*\n/\nPick an operation: ")
    val2 = int(input("What's the next number? "))
    calc = calculator(val, op, val2)
    cont = input(f"Type 'y' to continue calculating with {calc}, or type 'n' to start a new calculation: ")
    # print(cont)
    # print(len(cont))
    # print(start)
    if cont.lower() == "y":
        start += 1
        val = calc
        calc_app(start)
    if cont.lower() == "n":
        return calc
            
# print(calculator(3, "+", 2))
calc_app()