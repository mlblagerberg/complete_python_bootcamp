"""Project: Korean Flashcards
Start: May 16th, 2024
Last touched: May 16th, 2024
Author: Madeleine L.
"""
# Resources:
# https://ko.wiktionary.org/wiki/%EB%B6%80%EB%A1%9D:%EC%9E%90%EC%A3%BC_%EC%93%B0%EC%9D%B4%EB%8A%94_%ED%95%9C%EA%B5%AD%EC%96%B4_%EB%82%B1%EB%A7%90_5800
# colorhunt.co

import pandas as pd
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
IMAGE_PATH = "~/GitHub/complete_python_bootcamp/Day31_Korean_Flashcards/images"

# words = pd.read_excel("한국어 학습용 어휘 목록.xls")
words = pd.read_csv("한국어 학습용 어휘 목록 - 한국어학습용어휘등급표 원어 정보 정리 쿼리.csv")
sorted_words = words.sort_values("순위 (ranking)")
cleaned_words = sorted_words.drop(labels=["품사 (Part of speech)", "단어 (word)", "풀이 (Explanation)", "등급 (Rating)",
                                          "suffix number"], axis=1)
print(cleaned_words.head())

# Create UI window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Build canvas and add images
canvas = Canvas(height=700, width=900, bg=BACKGROUND_COLOR, highlightthickness=0)
x_image = PhotoImage(file=f"{IMAGE_PATH}/wrong.png")
check_image = PhotoImage(file=f"{IMAGE_PATH}/right.png")
card_back = PhotoImage(file=f"{IMAGE_PATH}/card_back.png")
card_front = PhotoImage(file=f"{IMAGE_PATH}/card_front.png")
canvas.create_image(225, 650, image=x_image)
canvas.create_image(675, 650, image=check_image)
canvas.create_image(450, 300, image=card_back)
canvas.create_image(450, 300, image=card_front)
canvas.pack()

# Create titles for words
title_label = Label(text="Title", bg="white", font=("Ariel", 40, "italic"))
word_label = Label(text="Word", bg="white", font=("Ariel", 60, "bold"))
title_label.place(x=400, y=150)
word_label.place(x=355, y=263)



window.mainloop()
