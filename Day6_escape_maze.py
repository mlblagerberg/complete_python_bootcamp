"""
Project: 
Start: January 22th, 2024
Last touched: January 22th, 2024 
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
            
