"""Project: Paddle Class for Pong Game
Start: March 5th, 2024
Last touched: March 5th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
NORTH = 90
SOUTH = 180
MOVE_DISTANCE = 20


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

    def move_up(self):
        # self.right_paddle.setheading(NORTH)
        new_y = self.ycor() + MOVE_DISTANCE
        # self.right_paddle.forward(MOVE_DISTANCE)
        self.goto(self.xcor(), new_y)

    def move_down(self):
        # self.right_paddle.setheading(NORTH)
        new_y = self.ycor() - MOVE_DISTANCE
        # self.right_paddle.forward(MOVE_DISTANCE)
        self.goto(self.xcor(), new_y)


