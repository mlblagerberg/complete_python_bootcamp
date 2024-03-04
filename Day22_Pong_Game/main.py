"""Project: Pong Game
Start: March 4th, 2024
Last touched: March 4th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen

# TODO 1: Create screen with correct color and boundary line
screen = Screen()
screen.setup(1200, 700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# TODO 2: Create class for pong paddles
pieces = []
y = -20
for i in range(0, 3):
    paddle = Turtle(shape="square")
    paddle.penup()
    paddle.setposition(-580, y)
    paddle.color("white")
    y += 20
    screen.update()


# TODO 3: Control paddles with keys
# TODO 4: Create class for pong ball and get ball to move back and forth depending on paddle hits
# TODO 5: Create class for scoreboard and score tracking method
# TODO 6: If pong ball hits paddle then bounce, if paddle misses update score

screen.exitonclick()