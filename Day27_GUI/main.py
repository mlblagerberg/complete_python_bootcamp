"""Project: Miles to Kilometers Project
Start: April 26th, 2024
Last touched: April 26th, 2024
Author: Madeleine L.
"""
# Reference: https://tcl.tk/man/tcl8.6/TkCmd/entry.htm

from tkinter import *
window = Tk()
window.title("Practice GUI Program")
window.minsize(width=500, height=300)

# Create label
my_label = Label(text="Test label", font=("Arial", 24, "bold"))
# place formatted label on screen
my_label.pack(side="top")

my_label["text"] = "New Test Label"
my_label.config(text="Newest Test Label")

# Entry
input = Entry(width=10)
input.pack()


# Button
def button_clicked():
    user_input = input.get()
    my_label.config(text=f"{user_input}")


button = Button(text="Enter", command=button_clicked)
button.pack()



# to keep window on screen
window.mainloop()
