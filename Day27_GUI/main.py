"""Project: Miles to Kilometers Project
Start: April 26th, 2024
Last touched: April 26th, 2024
Author: Madeleine L.
"""
# Reference: https://tcl.tk/man/tcl8.6/TkCmd/entry.htm

from tkinter import *
FONT = "Arial"
FONT_SIZE = 15


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# Create labels
miles_label = Label(text="Miles", font=(FONT, FONT_SIZE))
equal_label = Label(text="is equal to",  font=(FONT, FONT_SIZE))
km_label = Label(text="Km", font=(FONT, FONT_SIZE))
result_label = Label(text=0, font=(FONT, FONT_SIZE))
miles_label.grid(column=2, row=0)
equal_label.grid(column=0, row=1)
km_label.grid(column=2, row=1)
result_label.grid(column=1, row=1)

# Entry
entry = Entry(width=10)
# entry.pack()
entry.grid(column=1, row=0)


# Button
def button_clicked():
    mile_input = int(entry.get())
    km = mile_input * 1.609344
    result_label.config(text=f"{km}")


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


# to keep window on screen
window.mainloop()
