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
CREAM = "#fff2d7"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

def change_color(canvas, item_id, new_color):
    canvas.itemconfig(item_id, fill=new_color)


window = Tk()
window.title("My Password Manager")
window.config(padx=100, pady=50, bg=CREAM)

canvas = Canvas(height=300, width=300, bg=CREAM, highlightthickness=0)
lock_pic = PhotoImage(file="logo.png")
canvas.create_image(145, 125, image=lock_pic)
# logo = Image.open("logo.png")
# lock_bitmap = ImageTk.BitmapImage(logo)
# bitmap_item_id = canvas.create_bitmap(145, 125, bitmap=lock_bitmap)  # anchor=CENTER)
canvas.pack()


window.mainloop()
