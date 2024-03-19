"""Project: Snake Game
Start: February 29th, 2024
Last touched: March 19th, 2024
Author: Madeleine L.
"""
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
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

    if abs(snake.head.distance(food)) < 15:
        food.reset()
        score.update_score()
        snake.extend_snake()
        food = Food()

    # Detect collision with wall
    if abs(snake.head.pos()[0] + 8) >= 300 or abs(snake.head.pos()[1] + 8) >= 300:
        # move_forward = False
        score.reset()
        snake.reset()

    # Detect collision with tail
    for turtle in snake.turtles[1:]:  # i in range(1, len(snake.turtles) - 1): Using slicing instead, easier to read
        if snake.head.distance(turtle) < 10:
            # move_forward = False
            score.reset()
            snake.reset()


screen.exitonclick()
