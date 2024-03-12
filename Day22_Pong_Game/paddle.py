"""Project: Paddle Class for Pong Game
Start: March 5th, 2024
Last touched: March 11th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
NORTH = 90
SOUTH = 180
MOVE_DISTANCE = 50


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x_cor, y_cor)
        self.color("white")
        self.speed("fastest")

    def move_up(self):
        if self.ycor() + MOVE_DISTANCE > 290:
            new_y = self.ycor()
        else:
            new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() - MOVE_DISTANCE < - 290:
            new_y = self.ycor()
        else:
            new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
