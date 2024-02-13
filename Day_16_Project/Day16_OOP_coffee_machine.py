"""
Project: OOP Coffee Machine
Start: February 13th, 2024
Last touched: February 13th, 2024
Author: Madeleine L.
"""

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink3")
timmy.width(3)


def concentric_triangles(count_tri, initial_size):
    for i in range(0, count_tri):
        median = (initial_size ** 2 - (initial_size / 2) ** 2) ** (1 / 2)
        # Draw a triangle
        x = -(initial_size/(2*(i+1)))
        y = -(median/(3*(i+1)))
        timmy.setpos(i*x, i*y)
        # print(timmy.pos())
        turns = 3
        while turns > 0:
            # timmy.width(turns)
            timmy.forward(initial_size)
            timmy.left(120)
            turns -= 1
        initial_size *= 2


concentric_triangles(4,50)
my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()

