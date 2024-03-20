"""Project: Scoreboard Class for Snake Game
Start: March 2nd, 2024
Last touched: March 20th, 2024
Author: Madeleine L.
"""
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

with open("high_score_data.txt", mode="r") as file:
    high_score = int(file.read())


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=-10, y=270)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.high_score = high_score

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.clear()
            self.high_score = self.score
            self.write(f"New high score! {self.high_score}", align=ALIGNMENT, font=FONT)
            self.score = 0
            with open("high_score_data.txt", mode="w") as update_file:
                update_file.write(str(self.high_score))
        else:
            self.clear()
            self.score = 0
            self.write("Game Over", align=ALIGNMENT, font=FONT)
