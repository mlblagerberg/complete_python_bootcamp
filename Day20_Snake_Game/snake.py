"""Project: Snake Class for Snake Game
Start: February 29th, 2024
Last touched: March 1st, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.length = 3
        self.turtles = []
# Todo 1: create snake body
        for turtle_index in range(0, self.length):
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            x = -20 * turtle_index
            t.setposition(x, 0)
            self.turtles.append(t)


# turtles[0].setheading(90)
    # Todo 2: continuous move forward
    def move(self):
        for turtle in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[turtle - 1].xcor()
            new_y = self.turtles[turtle - 1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.turtles[0].forward(20)
        if abs(self.turtles[0].pos()[0] + 10) >= 300 or abs(self.turtles[0].pos()[1] + 10) >= 300:
            exit()
