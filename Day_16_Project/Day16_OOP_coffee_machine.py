"""
Project: OOP Coffee Machine
Start: February 13th, 2024
Last touched: February 13th, 2024
Author: Madeleine L.
"""
## Using packages from https://pypi.org/

from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
# print(timmy)
timmy.shape("turtle")
timmy.color("DeepPink3")
timmy.width(3)


def concentric_triangles(count_tri, initial_size, offsetX=1, offsetY=1):
    """This function takes triangle count, initial size, and offset for X and Y coordinates as inputs and draws out
    triangles.
    offset X and Y : both default to 1 to draw concentric circles
    count_tri : number of concentric triangles
    initial_size : initial triangle side length"""
    previous_median = x = 0
    previous_size = y = 0
    for i in range(0, count_tri):
        median = (initial_size ** 2 - (initial_size / 2) ** 2) ** (1 / 2)
        # Draw a triangle
        if i == 0:
            timmy.setpos(0, 0)
        else:
            timmy.up()
            x -= (initial_size/2 - previous_size/2)*offsetX
            y -= (median/3 - previous_median/3)*offsetY
            timmy.setpos(x, y)
            timmy.down()
        # print(timmy.pos())
        turns = 3
        while turns > 0:
            # timmy.width(turns)
            timmy.forward(initial_size)
            timmy.left(120)
            turns -= 1
        previous_median = median
        previous_size = initial_size
        initial_size *= 2


# concentric_triangles(6, 20)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon_Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

