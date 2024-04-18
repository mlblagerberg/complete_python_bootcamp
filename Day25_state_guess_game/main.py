"""Project: States Game
Start: April 18th, 2024
Last touched: April 18th, 2024
Author: Madeleine L.
"""

import turtle
import pandas as pd
from state_names import StateName

screen = turtle.Screen()
screen.title("U.S. States Game")
# Load image as shape
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Find coordinates of each state to write state names
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

state_locations = pd.read_csv("50_states.csv")
# print(state_locations.head())

play_game = True
states_guessed = 0
answers = []
while play_game:
    input_state = screen.textinput(f"{states_guessed}/50 States Correct", "What is a state name?").capitalize()
# print(input_state)
# Use length to determine if no rows are returned (e.g. not a state)
    answer_data = state_locations[state_locations["state"] == input_state]
    if len(answer_data) != 0:
        x = answer_data["x"].to_list()[0]
        # print(x)
        y = answer_data["y"].to_list()[0]
        # print(y)
        us_state = StateName(x_cor=x, y_cor=y)
        us_state.write(f"{input_state}", True, align="center")
        print(answers)
        if input_state not in answers:
            answers.append(input_state)
            states_guessed += 1
    elif states_guessed == 50:
        print("You win!")




screen.exitonclick()