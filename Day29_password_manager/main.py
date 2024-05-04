"""Project: Password Manager
Start: May 1st, 2024
Last touched: May 3rd, 2024
Author: Madeleine L.
"""
# Resource: https://colorhunt.co/
from tkinter import *
import password_generator as pg
YELLOW = "#ffaf45"
ORANGE = "#fb6d48"
PINK = "#d74b76"
PURPLE = "#673f69"
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

        pwd_instance = pg.Password(letters_bol=let, numbers_bol=num, symbols_bol=sym, pwd_length=pwd)
        password = pwd_instance.generate_password()

        pwd_text.delete(0, END)
        pwd_text.insert(0, f"{password}")
        return password

    pwd_button = Button(pwd_window, text="Create Password", bg=CREAM, fg=BLUE, highlightbackground=CREAM, width=60
                        , command=get_password)
    pwd_button.grid(column=0, row=4, columnspan=4)

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


pwd_label = Label(text="Password:", bg=CREAM, fg=BLUE, font=("Ariel", 15))
pwd_text = Entry(highlightbackground=CREAM, width=35)
pwd_label.grid(row=3, column=0)
pwd_text.grid(row=3, column=1, columnspan=2)

gen_pwd = Button(text="Generate Password", highlightbackground=CREAM, fg=BLUE, width=11, command=password_window)
gen_pwd.grid(row=3, column=2)

add_pwd = Button(text="Add Password", highlightbackground=CREAM, fg=BLUE, width=33, command=store_credentials)
add_pwd.grid(row=4, column=1, columnspan=2)


window.mainloop()