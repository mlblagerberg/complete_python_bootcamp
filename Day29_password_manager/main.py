"""Project: Password Manager
Start: May 1st, 2024
Last touched: May 6th, 2024
Author: Madeleine L.
"""
from json import JSONDecodeError
# Resource: https://colorhunt.co/
from tkinter import *
from tkinter import messagebox
import password_generator as pg
from pyperclip import copy
import json
BLUE = "#3C5B6F"
CREAM = "#fff2d7"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_window():
    # ------------------------ PWD GEN UI --------------------------------------- #
    pwd_window = Toplevel(window)
    pwd_window.title("Password Generator")
    pwd_window.config(padx=20, pady=20, bg=CREAM)

    char_label = Label(pwd_window,text="Please select the characters you want to use:", bg=CREAM, fg=BLUE)
    char_label.grid(column=0, row=1)

    symbols = IntVar(value=1)
    numbers = IntVar(value=1)
    letters = IntVar(value=1)
    pwd_int = IntVar()

    sym_check = Checkbutton(pwd_window, text="Symbols", bg=CREAM, fg=BLUE, highlightbackground=CREAM
                            , variable=symbols)
    num_check = Checkbutton(pwd_window, text="Letters", bg=CREAM, fg=BLUE, highlightbackground=CREAM, variable=letters)
    let_check = Checkbutton(pwd_window, text="Numbers", bg=CREAM, fg=BLUE, highlightbackground=CREAM, variable=numbers)
    sym_check.grid(column=1, row=1)
    num_check.grid(column=2, row=1)
    let_check.grid(column=3, row=1)

    length_label = Label(pwd_window,text="Please select a password length:", bg=CREAM, fg=BLUE)
    length_label.grid(column=0, row=2)

    pwd_length = Scale(pwd_window, from_=5, to=30, bg=CREAM, fg=BLUE, length=300, orient=HORIZONTAL
                       , variable=pwd_int)
    pwd_length.grid(column=1, row=2, columnspan=3)

    def get_password():
        sym = symbols.get()
        num = numbers.get()
        let = letters.get()
        pwd = pwd_int.get()
        if sym + num + let == 0:
            messagebox.showinfo(title="Error", message="You must select at least one character type to generate a "
                                                       "password.")
        else:
            pwd_instance = pg.Password(letters_bol=let, numbers_bol=num, symbols_bol=sym, pwd_length=pwd)
            password = pwd_instance.generate_password()

            pwd_text.delete(0, END)
            pwd_text.insert(0, f"{password}")
            # copy password to clipboard
            copy(password)
            return password

    pwd_button = Button(pwd_window, text="Create Password", bg=CREAM, fg=BLUE, highlightbackground=CREAM, width=60
                        , command=get_password)
    pwd_button.grid(column=0, row=4, columnspan=4)

# ---------------------------- SAVE CREDENTIALS --------------------------------- #


def store_credentials():
    user_website = web_text.get()
    user_creds = user_text.get()
    user_pwd = pwd_text.get()
    new_data = {
        user_website: {
            "email": user_creds,
            "password": user_pwd,
        }
    }

    if len(user_website) == 0 or len(user_creds) == 0 or len(user_pwd) == 0:
        messagebox.showinfo(title="Error", message="All entries must be complete before submitting.\n\nPlease go back "
                                                   "and fill out missing fields")
    else:
        try:
            with open("/Users/Shared/data.json", "r") as cred_file:
                # Read stored data
                data = json.load(cred_file)
                # Update stored data with new entry
                data.update(new_data)  # Saves in dictionary format
        except FileNotFoundError:
            with open("/Users/Shared/data.json", "w") as cred_file:
                # Save updated data
                json.dump(new_data, cred_file, indent=4)
        except JSONDecodeError:
            with open("/Users/Shared/data.json", "w") as cred_file:
                json.dump(data, cred_file, indent=4)
        else:
            with open("/Users/Shared/data.json", "w") as cred_file:
                json.dump(data, cred_file, indent=4)

        web_text.delete(0, END)
        pwd_text.delete(0, END)


# ---------------------------- SEARCH CREDENTIALS --------------------------------- #
def search_credentials():
    try:
        with open("/Users/Shared/data.json", "r") as cred_file:
            # Read stored data
            data = json.load(cred_file)
            if web_text.get() in data:
                stored_user = data[web_text.get()]["email"]
                stored_pwd = data[web_text.get()]["password"]
                messagebox.showinfo(title=f"Credentials for {web_text.get()}", message=f"User: {stored_user}\n"
                                                                                       f"Password: {stored_pwd}")
            else:
                messagebox.showinfo(title=f"Entry does not exist", message=f"There is no credential pair stored for "
                                                                           f"{web_text.get()}.")
    except FileNotFoundError:
        with open("/Users/Shared/data.json", "w") as cred_file:
            messagebox.showinfo(title="Error", message="No password file is created yet.")
#     cred_file = open("/Users/Shared/data.txt")
#     for line in cred_file.readlines():
#         cred_line = line.split(", ")
#         print(cred_line[0])
#         if cred_line[0].lower() == web_text.lower():
#             messagebox.showinfo(title="Error",
#                                 message="That website already exists")


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


pwd_label = Label(text="Password:", bg=CREAM, fg=BLUE, font=("Ariel", 15))
pwd_text = Entry(highlightbackground=CREAM, width=35)
pwd_label.grid(row=3, column=0)
pwd_text.grid(row=3, column=1, columnspan=2)

gen_pwd = Button(text="Generate Password", highlightbackground=CREAM, fg=BLUE, width=11, command=password_window)
gen_pwd.grid(row=3, column=2)

add_pwd = Button(text="Add Password", highlightbackground=CREAM, fg=BLUE, width=33, command=store_credentials)
add_pwd.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", highlightbackground=CREAM, fg=BLUE, width=10, command=search_credentials)
search.grid(row=1, column=2)

window.mainloop()
