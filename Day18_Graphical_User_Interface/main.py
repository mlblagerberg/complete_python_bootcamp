"""Project: Turtle and GUI
Start: February 22nd, 2024
Last touched: February 22nd, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen
from random import random, choice

tim = Turtle()
tim.shape("turtle")
# tim.color("light green")
# tim.color("deep pink")
# Draw square
# n = 4
# while n > 0:
#     tim.forward(100)
#     tim.right(90)
#     n -= 1
#
# tim.color("dark cyan")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw dashed line
# tim.up()
# tim.setposition(x=(-250), y=0)
# for _ in range(50):
#     tim.down()
#     tim.forward(5)
#     tim.up()
#     tim.forward(5)


def change_color():
    r = random()
    b = random()
    g = random()

    tim.color(r, b, g)


# for i in range(0, 10):
#     change_color()
#     side = 3 + i
#     for j in range(0, side):
#         tim.forward(100)
#         angle = 360 / side
#         tim.right(angle)
#         # tim.forward(50)


# Illustrate a random walk
def random_walk(steps):
    tim.pensize(10)
    tim.speed(8)
    direction = [0, 90, 180, 270]
    for i in range(0,steps + 1):
        change_color()
        turn = choice(direction)
        tim.right(turn)
        tim.forward(50)


random_walk(100)

screen = Screen()
screen.exitonclick()
