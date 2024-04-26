"""Project: Tkinter Practice
Start: April 25th, 2024
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
# user_input = input.get()


# Button
def button_clicked():
    user_input = input.get()
    my_label.config(text=f"{user_input}")


button = Button(text="Enter", command=button_clicked)
button.pack()

# Text entry
entry = Entry(width=30)
# Add text in entry box, e.g instructions
entry.insert(END, string="Please input your text here.")
# Get text entry
print(entry.get())
entry.pack()
# Text box
text = Text(height=5, width=30)
# Put cursor in textbox
text.focus()
# Starting text
text.insert(END, "Please write a couple sentences.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spin box
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbox
def check_used():
    print(checked_state.get())


# Variable to hold onm to checked state, 0 for no check and 1 for box is checked
checked_state = IntVar()
checkbutton = Checkbutton(text="Yes?", variable=checked_state, command=check_used)
checked_state.get()
checkbutton.pack()


# Radio button
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Option3", value=3, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Cantaloupe", "Banana", "Grape", "Apple", "Guava", "Pineapple"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

# Bind function to a listbox
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# to keep window on screen
window.mainloop()
