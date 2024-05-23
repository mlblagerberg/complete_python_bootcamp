"""Project: Tkinter Trivia App UI
Start: May 22nd, 2024
Last touched: May 23rd, 2024
Author: Madeleine L.
"""

from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
IMAGE_PATH = "~/GitHub/complete_python_bootcamp/Day34_Trivia_App/images"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(height=500, width=350)
        self.window.config(pady=40, padx=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Ariel", 15))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text((150, 125), width=280, text=f"Question", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=40)

        false_png = PhotoImage(file=f"{IMAGE_PATH}/false.png")
        true_png = PhotoImage(file=f"{IMAGE_PATH}/true.png")
        self.false_button = Button(image=false_png, command=self.false_clicked)
        self.false_button.grid(column=1, row=2)
        self.true_button = Button(image=true_png, command=self.true_clicked)
        self.true_button.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def true_clicked(self):
        if self.quiz.check_answer("True"):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.get_next_question()

    def false_clicked(self):
        if self.quiz.check_answer("False"):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
        self.get_next_question()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)
        print(q_text)





