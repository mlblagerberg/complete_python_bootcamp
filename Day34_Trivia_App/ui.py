"""Project: Tkinter Trivia App UI
Start: May 22nd, 2024
Last touched: May 22nd, 2024
Author: Madeleine L.
"""

from tkinter import *
THEME_COLOR = "#375362"
IMAGE_PATH = "/Users/madeleinebeattylagerberg/GitHub/complete_python_bootcamp/Day34_Trivia_App/images"


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.minsize(height=600, width=350)
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Ariel", 15))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text((150, 125), text="Question 1", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        false_png = PhotoImage(file=f"{IMAGE_PATH}/false.png")
        true_png = PhotoImage(file=f"{IMAGE_PATH}/true.png")
        self.false_button = Button(image=false_png)
        self.false_button.grid(column=1, row=2)
        self.true_button = Button(image=true_png)
        self.true_button.grid(column=0, row=2)

        self.window.mainloop()




