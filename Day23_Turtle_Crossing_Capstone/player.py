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


class Player(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.setheading(NORTH)
        self.step = 40
        self.x_cord = 0
        self.y_cord = -(screen_height / 2) + 20
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.setposition(0, self.y_cord)

    def move_forward(self):
        self.setheading(NORTH)
        self.forward(self.step)

    def move_left(self):
        self.setheading(WEST)
        self.forward(self.step)

    def move_backward(self):
        self.setheading(SOUTH)
        self.forward(self.step)

    def move_right(self):
        self.setheading(EAST)
        self.forward(self.step)