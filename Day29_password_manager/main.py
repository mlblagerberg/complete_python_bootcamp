"""Project: Password Manager
Start: May 1st, 2024
Last touched: May 1st, 2024
Author: Madeleine L.
"""
# Resource: https://colorhunt.co/
from tkinter import *
from PIL import Image, ImageTk
YELLOW = "#ffaf45"
ORANGE = "#fb6d48"
PINK = "#d74b76"
PURPLE = "#673f69"
BLUE = "#3C5B6F"
CREAM = "#fff2d7"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

def change_color(canvas, item_id, new_color):
    canvas.itemconfig(item_id, fill=new_color)


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50, bg=CREAM)

canvas = Canvas(height=200, width=200, bg=CREAM, highlightthickness=0)
lock_pic = PhotoImage(file="logo.png")
canvas.create_image(98, 90, image=lock_pic)
canvas.grid(column=1, row=0)

website = Label(text="Website:", bg=CREAM, fg=BLUE, font=("Ariel", 15))
web_text = Entry(highlightbackground=CREAM, width=35)
web_text.focus()
website.grid(row=1, column=0)
web_text.grid(row=1, column=1, columnspan=2)

creds = Label(text="Email/Username:", bg=CREAM, fg=BLUE, font=("Ariel", 15))
creds_text = Entry(highlightbackground=CREAM, width=35)
creds.grid(row=2, column=0)
creds_text.grid(row=2, column=1, columnspan=2)

pwd = Label(text="Password:", bg=CREAM, fg=BLUE, font=("Ariel", 15))
pwd_text = Entry(highlightbackground=CREAM, width=35)
pwd.grid(row=3, column=0)
pwd_text.grid(row=3, column=1, columnspan=2)

gen_pwd = Button(text="Generate Password", highlightbackground=CREAM, fg=BLUE, width=11)
gen_pwd.grid(row=3, column=2)

add_pwd = Button(text="Add Password", highlightbackground=CREAM, fg=BLUE, width=33)
add_pwd.grid(row=4, column=1, columnspan=2)


window.mainloop()
