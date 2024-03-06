"""Project: Paddle Class for Pong Game
Start: March 5th, 2024
Last touched: March 5th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
NORTH = 90
SOUTH = 180
MOVE_DISTANCE
X = 350
Y = 0


class Paddle:

    def __init__(self):
        self.paddles = []
        self.right_paddle = self.create_paddles()[0]
        self.left_paddle = self.create_paddles()[1]

    def create_paddles(self):
        """Takes a single input right_side, default is True. Change to False if creating a left paddle"""
        for i in [1, -1]:
            x = i * X
            paddle = Turtle(shape="square")
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.penup()
            paddle.setposition(x, Y)
            paddle.color("white")
            self.paddles.append(paddle)
        return self.paddles

    def right_move_up(self):
        self.right_paddle.setheading(NORTH)
        self.right_paddle.forward(MOVE_DISTANCE)

    def right_move_down(self):
        self.right_paddle.setheading(SOUTH)
        self.right_paddle.forward(MOVE_DISTANCE)


