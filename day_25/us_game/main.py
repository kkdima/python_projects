import turtle
import pandas as pd
import time
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "day_25/us_game/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def display_final_score(score):
    final_score = turtle.Turtle()
    final_score.penup()
    final_score.hideturtle()
    final_score.goto(0, 0)  # Center of screen
    final_score.write(f"Game Over! Final Score: {score}/50", 
                     align="center", 
                     font=("Arial", 24, "bold"))

states_data = pd.read_csv("day_25/us_game/50_states.csv")
game_is_on = True
correct_guesses = 0
first_guess = True
guessed_states = [] 


# game loop
while game_is_on:
    title = f"{correct_guesses}/50 States Correct"

    # Check if all states are guessed
    if correct_guesses == 50:
        screen.textinput(title="Congratulations!", 
                        prompt="You've guessed all 50 states! Game Over!")
        game_is_on = False
        break
    
    # Change prompt based on whether it's the first guess
    if first_guess:
        prompt = "What's your first guess?"
        first_guess = False  # Set flag to False after first guess
    else:
        prompt = "What's another state's name? Type 'exit' to quit"
    
    answer_state = screen.textinput(title=title, prompt=prompt)
    if answer_state is None or answer_state.lower() == "exit":
        game_is_on = False
        display_final_score(correct_guesses)
        time.sleep(5)
        break
    answer_state = answer_state.title()

    if answer_state in states_data["state"].values:
        correct_guesses += 1
        state_guess_x = states_data[states_data["state"] == answer_state]["x"].values[0]
        state_guess_y = states_data[states_data["state"] == answer_state]["y"].values[0]
        state_guess = turtle.Turtle()
        state_guess.penup()
        state_guess.hideturtle()
        state_guess.goto(state_guess_x, state_guess_y)
        state_guess.write(answer_state)

    # Get list of states that weren't guessed
    all_states = states_data.state.to_list()
    missing_states = [state for state in all_states if state not in guessed_states]

    # Create a new DataFrame with missing states
    missing_states_df = pd.DataFrame(missing_states, columns=["Missed States"])

    # Save to CSV
    missing_states_df.to_csv("day_25/us_game/states_to_learn.csv", index=False)

if correct_guesses < 50:
    print(f"Game Over! Final Score: {correct_guesses}/50")
