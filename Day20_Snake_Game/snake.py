"""Project: Snake Class for Snake Game
Start: February 29th, 2024
Last touched: March 2nd, 2024
Author: Madeleine L.
"""

from turtle import Turtle

MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270

class Snake:
    def __init__(self):
        self.length = 3
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
        self.tail = self.turtles[-1]

    def create_snake(self):
        for turtle_index in range(0, self.length):
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            x = -20 * turtle_index
            t.setposition(x, 0)
            self.turtles.append(t)

    def add_turtle(self, position):
        t = Turtle(shape="square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.turtles.append(t)

    def extend_snake(self):
        self.add_turtle(self.tail.position())

    def move(self):
        for turtle in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[turtle - 1].xcor()
            new_y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)
        # if abs(self.head.pos()[0] + 10) >= 300 or abs(self.head.pos()[1] + 10) >= 300:
        #     exit()

    def east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
