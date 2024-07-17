import random
import re

# High scores for each difficulty level
high_scores = {"easy": float("inf"), "hard": float(
    "inf"), "expert": float("inf")}


def set_difficulty():
    difficulty = input("Choose difficulty (easy, hard, expert): ")
    if difficulty not in ["easy", "hard", "expert"]:
        print("Invalid difficulty. Defaulting to easy.")
        difficulty = "easy"
    return difficulty


def ask_user_to_guess():
    while True:
        try:
            guess = int(input("Guess a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    return guess


def check_answer(guess, number_to_guess, guesses):
    if guess < number_to_guess:
        print("Too low!")
        return guesses - 1
    elif guess > number_to_guess:
        print("Too high!")
        return guesses - 1
    else:
        print(f"Correct! You've guessed the number, it was {number_to_guess}.")
        return True
    return False


def play_game():
    # Stage 1: Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Stage 2: Ask the user to choose difficulty level
    difficulty = set_difficulty()

    # Set the number of guesses based on difficulty level
    guesses = {"easy": 10, "hard": 5, "expert": 3}[difficulty]

    # Stage 6: Track the number of turns the user has taken

    while True:
        # Stage 8: Ask the user to guess the number
        guess = ask_user_to_guess()

        # Stage 3: Check the user's guess against the random number
        if guess == number_to_guess:
            # Stage 4: If the guess is correct, end the game
            print("Correct! You've guessed the number.")
            return guesses - 1
            if guesses < high_scores[difficulty]:
                high_scores[difficulty] = guesses
                print("New high score for " + difficulty + " difficulty!")
            break
        else:
            check_answer(guess, number_to_guess, guesses)
            break

    # Stage 7: Let the user know how many turns they took to guess the number
    print("You took " + str(guesses) + " turns to guess the number.")

    # Stage 9: Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() == "yes":
        # Stage 10: If the user wants to play again, start the game again
        play_game()
    else:
        # Stage 11: If the user does not want to play again, end the game
        print("Thanks for playing!")


# Start the game
play_game()
