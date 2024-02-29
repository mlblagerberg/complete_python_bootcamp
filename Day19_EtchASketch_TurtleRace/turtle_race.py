"""Project: Scratch File: Turtle Race- State, Event Listeners
Start: February 28th, 2024
Last touched: February 28th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(700, 600)
screen.listen()
race_is_on = False
user_guess = screen.textinput("Make your guess", "Guess which turtle will win: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = 200
turtles = []
for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.up()
    t.shapesize(2)
    t.color(colors[turtle_index])
    t.setposition(-300, y)
    y -= 75
    turtles.append(t)

if user_guess:
    race_is_on = True


# def turtle_race():
    while race_is_on:
        for turd in turtles:
            step = randint(0, 15)
            turd.forward(step)
            if turd.pos()[0] >= 350:
                if turd.color()[1] == user_guess.lower():
                    print(f"You won! The {turd.color()[0]} turtle is the winner!")
                else:
                    print(f"You lost. The {turd.color()[0]} turtle is the winner.")
                race_is_on = False


def turtle_reset():
    y = 200
    for turdley in turtles:
        turdley.setposition(-300, y)
        y -= 75


# screen.onkey(key="s", fun=turtle_race)
screen.onkey(key="r", fun=turtle_reset)
screen.exitonclick()
