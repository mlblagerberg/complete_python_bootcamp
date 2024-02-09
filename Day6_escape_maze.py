"""
Project: 
Start: January 22th, 2024
Last touched: January 23th, 2024 
Author: Madeleine L.
"""

### Functions & While loops
## Using Reeborg's World


## Hurdle 1 needs turn right and jump
# Function for turning right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Define jump hurdle function
def jump():
    #move()
    turn_left()

    move()
    turn_right()
   
    move()
    turn_right()

    move()
    turn_left()


## Hurdle 2 needs to jump six times
# Define function to jump 6 hurdles exactly
def jump_stop():
    for hurdles in range(0,6):
        if at_goal() is True:
            break
        else:
            jump()


## Hurdle 3 nees to recognize when we've reached the goal and stop
def course():
    while at_goal() is False:
        if front_is_clear() is True:
            move()
        else:
            jump()
        

## Hurdle 4 needs to check for wall height 
# Define new jump hurdle function
def jump():
    move()
    turn_right()


# Define run any hurdle course            
def course():
    steps = 0
    while at_goal() is False:
        if front_is_clear() is True:
                move()
        else:
            turn_left()
            jump()
            
            steps += 1
            
            if front_is_clear() is True and steps != 0:
                jump()
                while steps > 0:
                    move()
                    steps -= 1
                turn_left()


## Maze
def start_north():
    while is_facing_north() is False:
        turn_left()


# Define maze function
def maze():
#    start_north()
#    if right_is_clear():
#        turn_right()
#        forward_move()
    while at_goal() is False:
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
#            if front_is_clear():
#                move()
#            else:
#                turn_left()
#                move()


# Challenge problem
def start_north():
    while is_facing_north() is False:
        turn_left()


# Define maze function
def maze():
    start_north()
    turn_left()
    while at_goal() is False:
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

