"""Project: Car Class for Turtle Crossing Capstone
Start: March 12th, 2024
Last touched: March 19th, 2024
Author: Madeleine L.
"""

from turtle import Turtle
from random import choice, randint, betavariate
import time

COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "deep pink", "black", "white", "gold"]
SPEED_INCREMENT = 5


class Car(Turtle):

    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.color(choice(COLORS))
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.lane_step = round(screen_height / 15)
        self.lane_details = self.car_lane()
        self.setx(self.lane_details[0])
        self.sety(self.lane_details[1])
        self.car_speed = randint(10, 20)

    def car_lane(self):
        lane = randint(2, 15)
        x_cord = self.screen_width / 2
        y_cord = -(self.screen_height + self.lane_step) / 2 + self.lane_step * lane
        return x_cord, y_cord

    def car_move(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.lane_details[1])

    def level_up(self):
        self.car_speed += SPEED_INCREMENT


class CarManager:

    def __init__(self, screen_width, screen_height):
        self.car_count = randint(1, 30)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.car_list = []

    def create_cars(self):
        for _ in range(self.car_count):
            car = Car(self.screen_width, self.screen_height)
            self.car_list.append(car)

    def move_cars(self):
        for i in self.car_list:
            i.car_move()
            if i.xcor() < -self.screen_width / 2:
                i.hideturtle()
                self.car_list.remove(i)

            # rand_time = randint(0, 5) / 10
            # print(rand_time)
            # time.sleep(rand_time)







