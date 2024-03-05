"""Project: Paddle Class for Pong Game
Start: March 5th, 2024
Last touched: March 5th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
NORTH = 90
SOUTH = 180


class Paddle:

    def __init__(self):
        self.pieces = []
        self.top = self.pieces[-1]
        self.bottom = self.pieces[0]

    def create_paddle(self, right_side=True):
        """Takes a single input right_side, default is True. Change to False if creating a left paddle"""
        i = 1
        if not right_side:
            i = -1
        y = -20
        x = i * 350
        for _ in range(0, 5):
            paddle = Turtle(shape="square")
            paddle.penup()
            paddle.setposition(x, y)
            paddle.color("white")
            y += 20
            self.pieces.append(paddle)

    def move_up(self):
        self.top.heading(NORTH)
        for piece in self.pieces[1:5, -1]:
            x = self.pieces[piece].xcor()
            new_y = self.pieces[piece - 1].ycor()
            self.pieces[piece].goto(x, new_y)
        self.top.forward(20)

    def move_down(self):
        self.bottom.headding(SOUTH)
        for piece in self.pieces[1:5]:
            x = self.pieces[piece].xcor()
            new_y = self.pieces[piece + 1].ycor()
            self.pieces[piece].goto(x, new_y)
        self.bottom.forward(20)

