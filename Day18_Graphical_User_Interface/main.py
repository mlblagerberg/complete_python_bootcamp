"""Project: Turtle and GUI
Start: February 22nd, 2024
Last touched: February 22nd, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen
from random import random, choice
from colorgram import extract

screen = Screen()
screen.colormode(255)

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
# def random_walk(steps):
#     tim.pensize(15)
#     tim.speed(10)
#     direction = [0, 90, 180, 270]
#     for i in range(0,steps + 1):
#         change_color()
#         turn = choice(direction)
#         tim.setheading(turn)
#         tim.forward(25)


# random_walk(500)

# def spiro(circle_count):
#     tim.pensize(2)
#     tim.speed("fastest")
#     degrees = 360 / circle_count
#     for i in range(0, circle_count + 1):
#         change_color()
#         tim.circle(100)
#         tim.left(degrees)
#
#
# spiro(12)

# colors = extract("Damien_Hirst_Dumb_Painting.jpg", 10)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
color_list = [(69, 78, 213), (234, 229, 232), (236, 35, 108), (221, 231, 238), (145, 28, 66), (230, 237, 232),
              (239, 75, 36), (7, 148, 95), (222, 170, 45), (183, 158, 47)]
# print(color_list[0][0])


# random_color = choice(color_list)
# tim.color(random_color)
# tim.dot(20)
# tim.up()
# tim.setpos((-350, -250))
# tim.forward(50)
# tim.down()
# tim.dot(20)

for i in range(0, 10):
    tim.speed("fastest")
    y = 50 * i
    x = -230
    y += -210
    tim.up()
    tim.hideturtle()
    tim.setpos((x, y))
    for _ in range(10):
        random_color = choice(color_list)
        tim.color(random_color)
        tim.dot(20)
        tim.forward(50)



screen.exitonclick()
