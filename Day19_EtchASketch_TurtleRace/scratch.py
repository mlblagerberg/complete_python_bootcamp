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


# Event listeners
# Higher order functions: when you pass a function as an input you only use name not () at en because () at end executes
# function immediately
screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()


