"""Project: Scoreboard Class for Snake Game
Start: March 2nd, 2024
Last touched: March 2nd, 2024
Author: Madeleine L.
"""
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=-10, y=270)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)
