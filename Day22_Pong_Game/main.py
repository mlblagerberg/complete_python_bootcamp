"""Project: Pong Game
Start: March 4th, 2024
Last touched: March 5th, 2024
Author: Madeleine L.
"""

from turtle import Screen
from paddle import Paddle

# TODO 1: Create screen with correct color and boundary line
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# TODO 2: Create class for pong paddles
right_paddle = Paddle(x_cor=350, y_cor=0)
left_paddle = Paddle(x_cor=-350, y_cor=0)

screen.tracer(1)

screen.listen()
screen.onkey(key="Up", fun=right_paddle.move_up)
screen.onkey(key="Down", fun=right_paddle.move_down)
screen.onkey(key="w", fun=left_paddle.move_up)
screen.onkey(key="s", fun=left_paddle.move_down)

# game_is_on = True
# if game_is_on:
#     screen.update()

# print(right_paddle)
# def go_up():
#     # right_paddle.setheading(90)
#     new_y = right_paddle.ycor() + 20
#     # right_paddle.forward(20)
#     right_paddle.goto(right_paddle.xcor(), new_y)


# # TODO 3: Control paddles with keys
# screen.listen()
# screen.onkey(key="space", fun=right_paddle.move_up)
# screen.onkey(key="Up", fun=go_up)
# TODO 4: Create class for pong ball and get ball to move back and forth depending on paddle hits
# TODO 5: Create class for scoreboard and score tracking method
# TODO 6: If pong ball hits paddle then bounce, if paddle misses update score

screen.exitonclick()