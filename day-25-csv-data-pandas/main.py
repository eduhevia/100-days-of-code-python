import turtle as t

import pandas as pd

# Setup screen and map background image
screen = t.Screen()
screen.title("U.S. States Game")
image = "day-25-csv-data-pandas/data/blank_states_img.gif"
screen.addshape(image)
t.shape(image)

# Initialize writer turtle to display state names on the map
writer = t.Turtle()
writer.penup()
writer.hideturtle()

# Load states data from CSV into a list
data = pd.read_csv("day-25-csv-data-pandas/data/50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

# Dynamic message to display feedback in the input box title
message = "What's another state's name?"

# Main game loop
while True:
    answer_state = (
        screen.textinput(
            title=f"{len(guessed_states)}/50 States Correct", prompt=message
        )
        .title()
        .strip()
    )
    # If user guessed all 50 states or wants to leave
    if not all_states or answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_states.to_csv(
            "day-25-csv-data-pandas/data/states_to_learn.csv", index=False, header=False
        )
        screen.bye()
        break

    # Handle correct guesses
    if answer_state in all_states:
        guessed_states.append(answer_state)
        all_states.remove(answer_state)

        message = "Correct! Keep going!"

        # Write state name on map
        state_data = data[data["state"] == answer_state]
        x = state_data["x"].item()
        y = state_data["y"].item()

        writer.goto(x, y)
        writer.write(answer_state)

    # Handle errors and repeated guesses
    elif answer_state in guessed_states:
        message = "You've guessed that state before!"

    elif answer_state == "":
        message = "You didn't type anything!"

    else:
        message = "That state doesn't exist!"


t.mainloop()
