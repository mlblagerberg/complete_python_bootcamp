"""Project: Scoreboard Class for Snake Game
Start: March 2nd, 2024
Last touched: March 2nd, 2024
Author: Madeleine L.
"""

from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=-10, y=270)
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "bold"))

    def update_score(self):
        self.score += 10
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "bold"))
