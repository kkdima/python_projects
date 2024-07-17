import random
import os
from art import logo, vs
from game_data import data
print(logo)


def generate_random_data():
    return random.sample(data, 2)

print(generate_random_data())


def get_user_input():
    # Inserted new line for gap in terminal
    return input("Who has more followers? Type 'A' or 'B': ").upper()
    # print("\n")


def compare_followers(user_input, data_list):
    if data_list[0]["follower_count"] > data_list[1]["follower_count"]:
        return "A"
    else:
        return "B"


def update_score(score):
    return score + 1


def remove_life(lives):
    return lives - 1


def update_record_score(score, record_score):
    if score > record_score:
        record_score = score


global record_score
record_score = 0


def game():
    global record_score
    score = 0
    lives = 3
    data_list = generate_random_data()

    while lives > 0:
        data_list = generate_random_data()
        print(f"{data_list[0]['name']}, a {
            data_list[0]['description']}, from {data_list[0]['country']}.")
        print("\n")

        print(vs)
        print(f"{data_list[1]['name']}, a {
              data_list[1]['description']}, from {data_list[1]['country']}.")
        print("\n")
        user_input = get_user_input()
        correct_answer = compare_followers(user_input, data_list)
        if user_input == correct_answer:
            os.system("clear")
            score = update_score(score)
            update_record_score(score, record_score)
            print(f"You're right! Current score: {score}")
            print(f"Your highest score: {record_score}")
            print("Lives left: " + "❤ " * lives)
            print("\n")
        else:
            os.system("clear")
            lives = remove_life(lives)
            print(f"Sorry, that's wrong. Final score: {score}")
            print(f"Your highest score: {record_score}")
            print("Lives left: " + "❤ " * lives)
            print("\n")

            if lives == 0:
                print("do you want to play again? (yes/no)")
                play_again = input()
                if play_again == "yes":
                    lives = score = 0
                    os.system("clear")
                    game()
                else:
                    print("Game Over!")


if __name__ == "__main__":
    game()
