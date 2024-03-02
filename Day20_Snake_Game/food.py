"""Project: Food Class for Snake Game
Start: March 2nd, 2024
Last touched: March 2nd, 2024
Author: Madeleine L.
"""


from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)


