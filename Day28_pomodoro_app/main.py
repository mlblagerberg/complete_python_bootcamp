"""Project: Pomodoro App
Start: April 29th, 2024
Last touched: April 29th, 2024
Author: Madeleine L.
"""

from tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(timer_length):
    if timer_length > 0:
        mins, secs = divmod(timer_length, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        canvas.itemconfig(timer_text, text=timer)
        window.after(1000, count_down, timer_length - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# TODO: Timer Title above tomato
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)
# TODO: Start and Reset Buttons
start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
# TODO: Check mark icons for each completed Pomodoro
check = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check.grid(column=1, row=3)
# TODO: Update 00:00 with countdown


canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_pic)
timer_text = canvas.create_text(105, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# count_down(5)









window.mainloop()
