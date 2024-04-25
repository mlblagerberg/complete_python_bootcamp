"""Project: GUI/Tkinter Practice
Start: April 25th, 2024
Last touched: April 25th, 2024
Author: Madeleine L.
"""

import tkinter
window = tkinter.Tk()
window.title("Practice GUI Program")
window.minsize(width=500, height=300)

# Create label
my_label = tkinter.Label(text="Test label", font=("Arial", 24, "bold"))
# place formatted label on screen
my_label.pack(side="top")

# Properties aren't listed in pack, these are advanced arguments
# Review - Keyword arguments:
# def my_function(a, b, c):
#     # Do this with a
#     # Then this with b
#     # Last this with c

# Create arguments with default values. You can change these but will default to the values without any inputs.
# def my_function(a=1, b=2, c=3):
#     # Do this with a
#     # Then this with b
#     # Last this with c

# In the documentation you can see optional arguments as 'ARG = ...'

# Unlimited arguments (also known as unlimited positional arguments)
def add(*args):
    total = 0
    for n in args:
        # print(n)
        total += n
    return total


print(add(3, 5, 6, 3))

# to keep window on screen
window.mainloop()
