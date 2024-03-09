"""Project: Ball class for Pong Game
Start: March 7th, 2024
Last touched: March 8th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1)
        self.goto(0, 0)
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.paddle_bounce()

