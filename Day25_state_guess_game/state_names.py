"""Project: States Game Class to Write Names
Start: April 18th, 2024
Last touched: April 18th, 2024
Author: Madeleine L.
"""

from turtle import Turtle


class StateName(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setx(x_cor)
        self.sety(y_cor)
        self.color("Black")




