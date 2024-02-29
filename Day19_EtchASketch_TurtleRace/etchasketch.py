"""Project: Scratch File: Etch-A-Sketch- State, Event Listeners
Start: February 27th, 2024
Last touched: February 28th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


# Functions for event listeners
def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(5)


def turn_right():
    tim.right(5)


def point_north():
    tim.setheading(90)


def point_south():
    tim.setheading(270)


def clear_screen():
    tim.clear()


# Event listeners
# Higher order functions: when you pass a function as an input you only use name not () at en because () at end executes
# function immediately
screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Up", fun=point_north)
screen.onkey(key="Down", fun=point_south)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()


