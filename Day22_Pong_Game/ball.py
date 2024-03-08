"""Project: Ball class for Pong Game
Start: March 7th, 2024
Last touched: March 7th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
from random import randint

X = 380
Y = 280

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(1)
        self.goto(0, 0)
        self.color("white")

    def move(self):
        # x = randint(-350, 350)
        # y = x
        self.goto(X, Y)