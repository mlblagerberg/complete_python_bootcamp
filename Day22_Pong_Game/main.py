"""Project: Pong Game
Start: March 4th, 2024
Last touched: March 5th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen
from paddle import Paddle

# TODO 1: Create screen with correct color and boundary line
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# TODO 2: Create class for pong paddles
paddles = Paddle()
right_paddle = paddles.right_paddle
left_paddle = paddles.left_paddle
screen.update()


# TODO 3: Control paddles with keys
screen.listen()
screen.onkey(key="q", fun=right_paddle.right_move_up)
screen.onkey(key="a", fun=right_paddle.right_move_down)
# TODO 4: Create class for pong ball and get ball to move back and forth depending on paddle hits
# TODO 5: Create class for scoreboard and score tracking method
# TODO 6: If pong ball hits paddle then bounce, if paddle misses update score

screen.exitonclick()