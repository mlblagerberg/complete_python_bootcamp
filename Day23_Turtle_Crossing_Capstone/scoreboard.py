"""Project: Scoreboard Class for Turtle Crossing Capstone
Start: March 12th, 2024
Last touched: March 15th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
FONT = ("Courier", 30, "normal")


class Scoreboard(Turtle):

    def __init__(self, screen_width, screen_height, level=0):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.level = level
        self.y_cord = screen_height / 2 - 40
        self.x_cord = -(screen_width / 2) + 40
        self.setposition(self.x_cord, self.y_cord)
        self.write(f"Level {level}", align="left", font=FONT)