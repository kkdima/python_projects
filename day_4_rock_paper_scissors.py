import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
#                "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[0][1])

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


setofchoices = [rock, paper, scissors]

print("Welcome to Rock, Paper, Scissors!")
userchoice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

print("Computer chose:")
computerchoice = random.randint(0, 2)


if userchoice >= 3 or userchoice < 0:
    print("You typed an invalid number. You lose!")
else:
    print(setofchoices[userchoice])
    print(setofchoices[computerchoice])
    if userchoice == 0 and computerchoice == 1:
        print("You lose!")
    elif computerchoice == 0 and userchoice == 2:
        print("You lose!")
    elif userchoice > computerchoice:
        print("You win!")
    elif computerchoice == userchoice:
        print("It's a draw!")
    else:
        print("You typed an invalid number. You lose!")
