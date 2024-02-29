"""Project: Scratch File: Turtle Race- State, Event Listeners
Start: February 28th, 2024
Last touched: February 28th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen
from random import randint
screen = Screen()
screen.setup(700, 600)
race_is_on = False

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


def race_reset():
    global race_is_on
    print("Resetting race...")
    y_cord = 200
    for turdley in turtles:
        turdley.setposition(-300, y_cord)
        y_cord -= 75
    race_is_on = False


def turtle_race():
    global race_is_on
    user_guess = screen.textinput("Make your guess", "Guess which turtle will win: ")
    if user_guess:
        race_is_on = True
    # winner = []
    while race_is_on:
        for turd in turtles:
            step = randint(0, 15)
            turd.forward(step)
            if turd.pos()[0] >= 330:
                winner = max(turtles, key=lambda x: x.pos()[0])
                if winner.color()[1] == user_guess.lower():
                    print(f"You won! The {winner.color()[0]} turtle is the winner!")
                else:
                    print(f"You lost. The {winner.color()[0]} turtle is the winner.")
                race_is_on = False
                break
        if not race_is_on:
            play_again = input(f"Do you want to play again? Answer 'yes' or 'no': ")
            if play_again.lower() == 'yes':
                race_reset()
                turtle_race()
            else:
                print("Thanks for playing!")
                screen.bye()


screen.listen()
screen.onkey(key="r", fun=turtle_race)
# screen.onkey(key="s", fun=race_reset) # won't work and can't figure out why
# screen.listen()
# screen.getcanvas().bind("<space>", lambda event: race_reset())
screen.exitonclick()
