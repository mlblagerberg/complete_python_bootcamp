"""Project: Lane Class for Turtle Crossing Capstone
Start: March 12th, 2024
Last touched: March 12th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
STEP = 10

class Lane(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("gold")
        self.width(4)
        self.setheading(180)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.lane_count = round(screen_height / 40)
        self.dash_count = round(screen_width / STEP)

    def create_lanes(self):
        for i in range(self.lane_count):
            x_cord = self.screen_width / 2
            y_cord = -(self.screen_height / 2) + 40 * i
            self.setposition(x_cord, y_cord)
            # line_dashes = self.dash_count
            for _ in range(self.dash_count):
                self.setheading(180)
                self.forward(STEP)
                self.pendown()
                self.forward(STEP)
                self.penup()


