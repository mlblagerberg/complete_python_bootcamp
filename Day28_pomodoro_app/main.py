"""Project: Pomodoro App
Start: April 29th, 2024
Last touched: April 30th, 2024
Author: Madeleine L.
"""

from tkinter import *
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    timer_label.config(text="Timer")
    check.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if (reps % 8) == 0:
        count_down(LONG_BREAK_MIN * 1)  # 20 seconds
        timer_label.config(text="Break", fg=RED)
    elif (reps % 2) == 0:
        count_down(SHORT_BREAK_MIN * 1)  # 5 seconds
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 1)  # 25 seconds
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(timer_length):
    if timer_length > 0:
        mins, secs = divmod(timer_length, 60)
        timer_time = '{:02d}:{:02d}'.format(mins, secs)
        canvas.itemconfig(timer_text, text=timer_time)
        global timer
        timer = window.after(1000, count_down, timer_length - 1)
    else:
        check_text = ""
        start_timer()
        pomodoro = floor(reps / 2)
        for _ in range(0, pomodoro):
            check_text += "✔"
        check.config(text=check_text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW, command=start_timer)
reset_button = Button(text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=reset_timer)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check.grid(column=1, row=3)


canvas = Canvas(width=210, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(105, 112, image=tomato_pic)
timer_text = canvas.create_text(105, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
