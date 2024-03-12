"""Project: Player Class for Turtle Crossing Capstone
Start: March 12th, 2024
Last touched: March 12th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
NORTH = 90
WEST = 180
SOUTH = 270
EAST = 0

STEP = 30


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.setheading(NORTH)
        self.shapesize(1.5)
        self.setposition(0, -270)

    def move_forward(self):
        self.setheading(NORTH)
        self.forward(STEP)

    def move_left(self):
        self.setheading(WEST)
        self.forward(STEP)

    def move_backward(self):
        self.setheading(SOUTH)
        self.forward(STEP)

    def move_right(self):
        self.setheading(EAST)
        self.forward(STEP)