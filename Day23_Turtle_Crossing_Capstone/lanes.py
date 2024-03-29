"""Project: Lane Class for Turtle Crossing Capstone
Start: March 12th, 2024
Last touched: March 15th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
DASH_STEP = 10


class Grass(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("light green")
        self.lane_step = round(screen_height / 15)
        self.width(self.lane_step)
        self.screen_width = screen_width
        self.penup()
        self.x_cord = screen_width / 2
        self.y_cord = (-screen_height + self.lane_step) / 2
        self.setposition(self.x_cord, self.y_cord)
        self.setheading(180)

    def draw_grass(self):
        self.pendown()
        self.forward(self.screen_width)


class Lane(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("gold")
        self.width(2)
        self.setheading(180)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.lane_count = 15
        self.lane_step = round(screen_height / 15)
        self.dash_count = round(screen_width / DASH_STEP)

    def create_lanes(self):
        for i in range(self.lane_count):
            x_cord = self.screen_width / 2
            y_cord = -(self.screen_height / 2) + self.lane_step * i
            self.setposition(x_cord, y_cord)
            # line_dashes = self.dash_count
            for _ in range(self.dash_count):
                self.setheading(180)
                self.forward(DASH_STEP)
                self.pendown()
                self.forward(DASH_STEP)
                self.penup()
