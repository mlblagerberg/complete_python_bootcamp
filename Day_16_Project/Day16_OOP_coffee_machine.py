"""
Project: OOP Coffee Machine
Start: February 13th, 2024
Last touched: February 13th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink3")

# Draw a trianle
turns = 3
while turns > 0:
    timmy.forward(100)
    timmy.left(120)
    turns -= 1


my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()

