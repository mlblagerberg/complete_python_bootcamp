"""Project: Scratch File: Turtle Race- State, Event Listeners
Start: February 28th, 2024
Last touched: February 28th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.colormode(255)
screen.listen()


def random_color(t):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    t.color(r, g, b)


tim1 = Turtle()
tim2 = Turtle()
tim3 = Turtle()
tim4 = Turtle()
tim5 = Turtle()

start = Turtle()
start.hideturtle()
start.up()
finish = Turtle()
finish.hideturtle()
finish.up()

# Draw start and finish lines
start.setposition(-300, -200)
start.setheading(90)
start.down()
start.forward(500)

finish.setposition(300, -200)
finish.setheading(90)
finish.down()
finish.forward(500)

turtles = [tim1, tim2, tim3, tim4, tim5]

y = 150
for t in turtles:
    t.up()
    random_color(t)
    t.shapesize(3)
    t.shape("turtle")
    t.setposition(-300, y)
    y -= 75


def turtle_race():
    for turd in turtles:
        if turd.pos()[0] >= 300:
            turd.setposition(0, 0)
        else:
            step = randint(1, 15)
            turd.forward(step)

        #     exit()
        # else:
        #     turtle_race()


def turtle_reset():
    y = 150
    for turd in turtles:
        turd.setposition(-300, y)
        y -= 75


screen.onkey(key="space", fun=turtle_race)
screen.onkey(key="r", fun=turtle_reset)
screen.exitonclick()
