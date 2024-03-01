"""Project: Snake Game
Start: February 29th, 2024
Last touched: March 1st, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(key="Up", fun=snake.north)
screen.onkey(key="Down", fun=snake.south)
screen.onkey(key="Left", fun=snake.west)
screen.onkey(key="Right", fun=snake.east)

move_forward = True
while move_forward:
    screen.update()
    time.sleep(0.1)

    snake.move()

# Todo 3: create snake food
# Todo 4: control snake
# screen.onkey(key="Up", fun=face_north)
# Todo 5: detect collision with food
# Todo 6: create scoreboard
# Todo 7: detect collision with wall or tail and end game




screen.exitonclick()