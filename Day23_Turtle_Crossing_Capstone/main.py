"""Project: Main File for Turtle Crossing Capstone
Start: March 11th, 2024
Last touched: March 15th, 2024
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
car_manager = CarManager(screen_width=WIDTH, screen_height=HEIGHT)
car_manager.create_cars()
car_list = car_manager.car_list
# car_sets.append(car_manager)

screen.listen()
screen.onkey(key="Up", fun=player.move_forward)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Down", fun=player.move_backward)
screen.onkey(key="Right", fun=player.move_right)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # for i in cars:
    #     i.move_cars()
    car_manager.move_cars()
    if player.ycor() >= HEIGHT / 2 - 20:
        player.next_level()
    if len(car_list) < 10:
        next_car_manager = CarManager(screen_width=WIDTH, screen_height=HEIGHT)
        next_car_manager.create_cars()
        for new_car in next_car_manager.car_list:
            car_list.append(new_car)
    # for car in car_list:
    #     if car.xcor() <= -WIDTH / 2 + 20:
    #         next_car_manager = CarManager(screen_width=WIDTH, screen_height=HEIGHT)
    #         next_car_manager.create_cars()
    #         for new_car in next_car_manager.car_list:
    #             car_list.append(new_car)
    # rand_time = randint(0, 15)
    # time.sleep(rand_time)
    # car_manager.create_cars()








# TODO: Place Turtle at the bottom of the screen and make it move forward by a jump amount with arrow keys
# TODO: Use random module to create cars to drive across with random speeds in random lanes
# TODO: Create scoreboard to score how far the turtle has traveled without getting hit
# TODO: Create coins for game that add to the score and obstacles that cannot be walked over by the turtle
# TODO: Create game levels so when turtle reaches te top of the screen increase car speed and move turtle back down to
#  bottom of the screen






screen.exitonclick()