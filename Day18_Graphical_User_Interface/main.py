"""Project: Turtle and GUI
Start: February 22nd, 2024
Last touched: February 22nd, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
# tim.color("light green")
tim.color("dark cyan")
tim.up()
tim.setposition(x=(-100), y=0)


# Draw square
# n = 4
# while n > 0:
#     tim.forward(100)
#     tim.right(90)
#     n -= 1
#
# tim.color("dark cyan")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# Draw dashed line
for _ in range(50):
    tim.down()
    tim.forward(5)
    tim.up()
    tim.forward(5)


screen = Screen()
screen.exitonclick()
