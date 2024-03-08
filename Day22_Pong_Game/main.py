"""Project: Pong Game
Start: March 4th, 2024
Last touched: March 7th, 2024
Author: Madeleine L.
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball

# TODO 1: Create screen with correct color and boundary line
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# TODO 2: Create class for pong paddles
right_paddle = Paddle(x_cor=350, y_cor=0)
left_paddle = Paddle(x_cor=-350, y_cor=0)
ball = Ball()

screen.tracer(1)

# # TODO 3: Control paddles with keys
screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)
screen.onkey(key="Up", fun=ball.move)


# TODO 4: Create class for pong ball and get ball to move back and forth depending on paddle hits
# TODO 5: Create class for scoreboard and score tracking method
# TODO 6: If pong ball hits paddle then bounce, if paddle misses update score

screen.exitonclick()