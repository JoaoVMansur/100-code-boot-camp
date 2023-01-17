import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Game")
image = "day 25/map_game/us-states-game-start/blank_states_img.gif"
tim = t.Turtle()
screen.addshape(image)
screen.setup(height= 600, width= 800)
t.shape(image)



data = pd.read_csv("day 25/map_game/us-states-game-start/50_states.csv")
all_states = data.state.to_list( )

guessed_states = []

while len(guessed_states) < 50:
    
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct ", prompt="What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t_1 = t.Turtle()
        t_1.hideturtle()
        t_1.penup()
        state_data = data[data.state == answer_state]
        t_1.goto(int(state_data.x), int(state_data.y)) 
        t_1.write(state_data.state.item())

    elif answer_state == "Exit":
        missing_states = [states for states in all_states if states not in guessed_states]

        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("day 25/map_game/us-states-game-start/state_to_learn.csv")
        break








