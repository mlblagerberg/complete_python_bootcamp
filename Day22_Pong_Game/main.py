"""Project: Pong Game
Start: March 4th, 2024
Last touched: March 11th, 2024
Author: Madeleine L.
"""

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

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

# TODO 4: Create class for pong ball and get ball and get it to bounce, end game if it hits walls and bounces off
#  paddles to move back and forth depending on paddle hits
screen.tracer(0)
right_score = Scoreboard(100, 220)
left_score = Scoreboard(-100, 220)
game_is_on = True

while game_is_on:
    # if BALL_SPEED < 0:
    #     BALL_SPEED = 0.001
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if abs(ball.ycor()) > 280:
        ball.bounce()
    # Detect paddle collisions
    if abs(ball.xcor() - right_paddle.xcor()) < 20 and abs(ball.ycor() - right_paddle.ycor()) < 50:
        ball.paddle_bounce()
    if abs(ball.xcor() - left_paddle.xcor()) < 20 and abs(ball.ycor() - left_paddle.ycor()) < 50:
        ball.paddle_bounce()
    # Stop game if ball hits wall
    if ball.xcor() > 390:
        ball.ball_reset()
        ball.bounce()
        left_score.update_score()
    if ball.xcor() < -390:
        ball.ball_reset()
        ball.bounce()
        right_score.update_score()

screen.exitonclick()
