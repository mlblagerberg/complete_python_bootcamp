"""Project: Scoreboard class for Pong Game
Start: March 9th, 2024
Last touched: March 9th, 2024
Author: Madeleine L.
"""

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0

    def create_score(self, x_cord, y_cord):
        self.setposition(x_cord, y_cord)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}")

