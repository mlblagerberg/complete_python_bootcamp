"""Project: Scoreboard Class for Turtle Crossing Capstone
Start: March 12th, 2024
Last touched: March 19th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
FONT = ("Courier", 30, "normal")


class Level(Turtle):

    def __init__(self, screen_width, screen_height, level=1):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        # self.score = 0
        self.level = level
        self.y_cord = screen_height / 2 - 40
        self.x_cord = -(screen_width / 2) + 40
        self.setposition(self.x_cord, self.y_cord)
        self.write(f"Level {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.level = 1
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)


class Score(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        # self.score = 0
        self.score = 0
        self.y_cord = screen_height / 2 - 40
        self.x_cord = (screen_width / 2) - 200
        self.setposition(self.x_cord, self.y_cord)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)
