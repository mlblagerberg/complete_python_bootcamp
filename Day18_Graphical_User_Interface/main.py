"""Project: Turtle and GUI
Start: February 22nd, 2024
Last touched: February 22nd, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.color("light green")


# Draw square
n = 4
while n > 0:
    tim.forward(100)
    tim.right(90)
    n -= 1

tim.color("dark cyan")
for _ in range(4):
    tim.forward(100)
    tim.right(90)

screen = Screen()
screen.exitonclick()
