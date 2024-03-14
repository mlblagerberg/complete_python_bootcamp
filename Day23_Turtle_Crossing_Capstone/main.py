"""Project: Main File for Turtle Crossing Capstone
Start: March 11th, 2024
Last touched: March 14th, 2024
Author: Madeleine L.
"""

import time
from turtle import Turtle, Screen
from player import Player
from lanes import Lane
from car_manager import Car, CarManager
from random import random, randint

WIDTH = 1000
HEIGHT = 1000

# TODO: Create grey background screen with dotted lines for lanes
screen = Screen()
screen.bgcolor("grey")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
player = Player(screen_width=WIDTH, screen_height=HEIGHT)
lane = Lane(screen_width=WIDTH, screen_height=HEIGHT)
lane.create_lanes()
# car = Car(screen_width=WIDTH, screen_height=HEIGHT)
# car_manager = CarManager(screen_width=WIDTH, screen_height=HEIGHT)
# car_manager.create_cars()
# car_manager.move_cars()

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Down", fun=player.move_backward)
screen.onkey(key="Right", fun=player.move_right)

# car_count = randint(10, 30)
# car_list = []
# for _ in range(car_count):
#     rand_time = random()
#     time.sleep(rand_time)
#     car = Car(screen_width=WIDTH, screen_height=HEIGHT)
#     # car.car_move()
#     car_list.append(car)

for _ in range(1, 11):
    rand_time = randint(0, 20) / 10
    time.sleep(rand_time)
    car = Car(screen_width=WIDTH, screen_height=HEIGHT)
    car.car_move()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()







# TODO: Place Turtle at the bottom of the screen and make it move forward by a jump amount with arrow keys
# TODO: Use random module to create cars to drive across with random speeds in random lanes
# TODO: Create scoreboard to score how far the turtle has traveled without getting hit
# TODO: Create coins for game that add to the score and obstacles that cannot be walked over by the turtle
# TODO: Create game levels so when turtle reaches te top of the screen increase car speed and move turtle back down to
#  bottom of the screen






screen.exitonclick()