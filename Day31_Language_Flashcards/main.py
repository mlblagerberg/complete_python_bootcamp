"""Project: Korean Flashcards
Start: May 16th, 2024
Last touched: May 21th, 2024
Author: Madeleine L.
"""
# Resources:
# https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800
# colorhunt.co

import pandas as pd
from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
CARD_BACKGROUND = "#91c1af"
IMAGE_PATH = "/Users/madeleinebeattylagerberg/GitHub/complete_python_bootcamp/Day31_Language_Flashcards/images"
random_word = {}

# -------------------------------------- IMPORT DATA ----------------------------------------- #
# words = pd.read_excel("한국어 학습용 어휘 목록.xls")
words = pd.read_csv("한국어 학습용 어휘 목록 - 한국어학습용어휘등급표 원어 정보 정리 쿼리.csv")
sorted_words = words.sort_values("순위 (ranking)")
cleaned_words = sorted_words.drop(labels=["순위 (ranking)", "품사 (Part of speech)", "단어 (word)", "풀이 (Explanation)", "등급 (Rating)",
                                          "suffix number"], axis=1)
word_dict = cleaned_words.to_dict(orient="records")
KEYS = list(word_dict[0].keys())
# print(type(KEYS))
# -------------------------------------- Button functionality ----------------------------------------- #


def next_card():
    global random_word, flip_timer
    # Cancel timer if it has already begun so we get proper 3 seconds on every flip
    window.after_cancel(flip_timer)
    random_word = choice(word_dict)
    word = random_word[KEYS[0]]

    canvas.itemconfig(card_image, image=card_front)
    title_label.config(text="Korean", bg="white", fg="black")
    word_label.config(text=f"{word}", bg="white", fg="black")
    word_label.place(x=375, y=263)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image, image=card_back)
    eng_word = random_word[KEYS[1]]
    title_label.config(text="English", bg=CARD_BACKGROUND, fg="white")
    word_label.config(text=f"{eng_word}", bg=CARD_BACKGROUND, fg="white")


# -------------------------------------- UI SETUP ----------------------------------------- #
# Create UI window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Build canvas and add images
canvas = Canvas(height=700, width=900, bg=BACKGROUND_COLOR, highlightthickness=0)
x_image = PhotoImage(file=f"{IMAGE_PATH}/wrong.png")
check_image = PhotoImage(file=f"{IMAGE_PATH}/right.png")
card_back = PhotoImage(file=f"{IMAGE_PATH}/card_back.png")
card_front = PhotoImage(file=f"{IMAGE_PATH}/card_front.png")
card_image = canvas.create_image(450, 300, image=card_front)
canvas.pack()

# Create titles for words and start of practice
title_label = Label(text="Korean", bg="white", font=("Ariel", 40, "italic"))
word_label = Label(text="", bg="white", font=("Ariel", 60, "bold"))
title_label.place(x=375, y=150)
word_label.place(x=375, y=263)

# Create buttons
wrong = Button(image=x_image, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, highlightthickness=0,
               command=next_card)
correct = Button(image=check_image, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, highlightthickness=0,
                 command=next_card)


wrong.place(x=175, y=600)
correct.place(x=625, y=600)

next_card()

window.mainloop()
