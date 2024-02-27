"""Project: Scratch File: State, Event Listeners
Start: February 27th, 2024
Last touched: February 27th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


# Event listener
screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()


