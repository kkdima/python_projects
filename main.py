print("The Love calculator is calculating your score...")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# all letters to small case
name1 = name1.upper()
name2 = name2.upper()

lowernames = name1 + name2  # combine both names

# check both names for the letters in the word LOVE
t = lowernames.count("T")
r = lowernames.count("R")
u = lowernames.count("U")
e = lowernames.count("E")

true = t + r + u + e  # add all the letters together

l = lowernames.count("L")
o = lowernames.count("O")
v = lowernames.count("V")
e = lowernames.count("E")

love = l + o + v + e  # add all the letters together

# combine the two numbers
score = int(str(true) + str(love))

# check the score and print the result
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
