"""Project: Snake Game
Start: February 29th, 2024
Last touched: February 29th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Todo 1: create snake body
turtles = []
for turtle_index in range(0, 3):
    t = Turtle(shape="square")
    t.penup()
    t.color("white")
    x = -20 * turtle_index
    t.setposition(x, 0)
    turtles.append(t)

screen.update()

# turtles[0].setheading(90)


# Todo 2: continuous move forward
def continuous_move_forward():
    move_forward = True
    while move_forward:
        screen.update()
        for turtle in range(len(turtles)-1, 0, -1):
            new_x = turtles[turtle - 1].xcor()
            new_y = turtles[turtle - 1].ycor()
            turtles[turtle].goto(new_x, new_y)
        turtles[0].forward(1)
        if abs(turtles[0].pos()[0] + 10) >= 300 or abs(turtles[0].pos()[1] + 10) >= 300:
            move_forward = False


screen.listen()
screen.onkey(key="space", fun=continuous_move_forward)
# Todo 3: create snake food
# Todo 4: control snake
# screen.onkey(key="Up", fun=face_north)
# Todo 5: detect collision with food
# Todo 6: create scoreboard
# Todo 7: detect collision with wall or tail and end game








screen.exitonclick()