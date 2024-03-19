"""Project: Main File for Turtle Crossing Capstone
Start: March 11th, 2024
Last touched: March 19th, 2024
Author: Madeleine L.
"""

import time
from turtle import Turtle, Screen
from player import Player
from lanes import Lane, Grass
from car_manager import Car, CarManager
from scoreboard import Scoreboard
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
grass = Grass(screen_width=WIDTH, screen_height=HEIGHT)
grass.draw_grass()
car_manager = CarManager(screen_width=WIDTH, screen_height=HEIGHT)
car_manager.create_cars()
car_list = car_manager.car_list
scoreboard = Scoreboard(screen_width=WIDTH, screen_height=HEIGHT)
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
    car_manager.move_cars()
    if player.ycor() >= HEIGHT / 2 - 20:
        player.next_level()
        scoreboard.increase_level()
    for car in car_list:
        # Depending on player's current level X, add ceiling of X/2 cars to the list every time a car crosses the
        # halfway point.
        if car.xcor() == 0:
            for _ in range(round(scoreboard.level/2)):
                car_list.append(Car(screen_width=WIDTH, screen_height=HEIGHT))
        if abs(player.xcor() - car.xcor()) < 20:  # and player.xcor() < car.xcor():
            if abs(player.ycor() - car.ycor()) < 20:  # Add proces here to restart game
                scoreboard.game_over()
                player.next_level()
                player.setheading(90)
    if len(car_list) < 10:
        next_car_manager = CarManager(screen_width=WIDTH, screen_height=HEIGHT)
        next_car_manager.create_cars()
        for new_car in next_car_manager.car_list:
            car_list.append(new_car)

# TODO: Create scoreboard method to score how far the turtle has traveled without getting hit
# TODO: Create coins for game that add to the score and obstacles that cannot be walked over by the turtle
# TODO: Create game levels so when turtle reaches the top of the screen increase car speed and move turtle back down to
#  bottom of the screen
# TODO: Increase number of single cars that spawn depending on the level the player is on.
# TODO: Create proper scoring method which adds 1 for every lane you reach without collision








screen.exitonclick()