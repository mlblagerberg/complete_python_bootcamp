"""Project: Password Manager
Start: May 1st, 2024
Last touched: May 3rd, 2024
Author: Madeleine L.
"""
# Resource: https://colorhunt.co/
from tkinter import *
import os
from PIL import Image, ImageTk
YELLOW = "#ffaf45"
ORANGE = "#fb6d48"
PINK = "#d74b76"
PURPLE = "#673f69"
BLUE = "#3C5B6F"
CREAM = "#fff2d7"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # ------------------------ PWD GEN UI --------------------------------------- #
    pwd_window = Tk()
    pwd_window.title("Password Generator")
    pwd_window.config(padx=20, pady=20, bg=CREAM)

    # pwd_canvas = Canvas(height=100, width=100, bg=CREAM, highlightthickness=0)
    # TODO Check boxes for symbols, letters, numbers
    # TODO Choose password length


# ---------------------------- SAVE CREDENTIALS --------------------------------- #


def store_credentials():
    user_website = web_text.get()
    user_creds = user_text.get()
    user_pwd = pwd_text.get()

    cred_file = open("/Users/Shared/data.txt", "a")
    cred_file.write(f"{user_website}, {user_creds}, {user_pwd}\n")


# ----------------------------- UI SETUP ---------------------------------------- #
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

user = Label(text="Email/Username:", bg=CREAM, fg=BLUE, font=("Ariel", 15))
with open("/Users/Shared/email.txt") as default_txt:
    email = default_txt.readlines()[0].strip()
user_text = Entry(highlightbackground=CREAM, width=35)
user_text.insert(END, string=f"{email}")
user.grid(row=2, column=0)
user_text.grid(row=2, column=1, columnspan=2)


pwd = Label(text="Password:", bg=CREAM, fg=BLUE, font=("Ariel", 15))
pwd_text = Entry(highlightbackground=CREAM, width=35)
pwd.grid(row=3, column=0)
pwd_text.grid(row=3, column=1, columnspan=2)

gen_pwd = Button(text="Generate Password", highlightbackground=CREAM, fg=BLUE, width=11)
gen_pwd.grid(row=3, column=2)

add_pwd = Button(text="Add Password", highlightbackground=CREAM, fg=BLUE, width=33, command=store_credentials)
add_pwd.grid(row=4, column=1, columnspan=2)


window.mainloop()
