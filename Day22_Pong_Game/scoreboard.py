"""Project: Scoreboard class for Pong Game
Start: March 9th, 2024
Last touched: March 9th, 2024
Author: Madeleine L.
"""

from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x_cord, y_cord)
        self.score = 0
        self.write(f"{self.score}", align="center", font=("Courier", 60, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 60, "normal"))
