"""Project: Player Class for Turtle Crossing Capstone
Start: March 12th, 2024
Last touched: March 19th, 2024
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
        self.color("purple")
        self.shape("turtle")
        self.setheading(NORTH)
        self.screen_height = screen_height
        self.step = round(screen_height / 15)
        self.x_cord = 0
        self.y_cord = -(screen_height / 2) + 20
        self.steps_taken = 0
        self.width_stretch_factor = (1.5 / 600) * screen_width
        self.height_stretch_factor = (1.5 / 600) * screen_height
        self.shapesize(stretch_wid=self.width_stretch_factor, stretch_len=self.height_stretch_factor)
        self.setposition(0, self.y_cord)

    def move_forward(self):
        self.setheading(NORTH)
        self.forward(self.step)
        self.steps_taken += 1

    def move_left(self):
        self.setheading(WEST)
        self.forward(self.step)

    def move_backward(self):
        self.setheading(SOUTH)
        self.forward(self.step)
        self.steps_taken -= 1

    def move_right(self):
        self.setheading(EAST)
        self.forward(self.step)

    def next_level(self):
        self.y_cord = -(self.screen_height / 2) + 20
        self.setposition(self.x_cord, self.y_cord)
