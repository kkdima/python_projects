import random

student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0

for x in student_heights:
    total_height += x

total_students = 0

for student in student_heights:
    total_students += 1


average_height = round(total_height / total_students)

# print(average_height)


# ADDING EVEN NUMBERS EXERCISE:
# x = int(input("Enter a number: "))
# if x > 1000 or x < 0:
#     print("Please enter a number between 0 and 1000")
#     exit()

# sum_of_even_numbers = 0

# for number in range(1, x + 1):
# 	if number % 2 == 0:
# 		sum_of_even_numbers += number

# print(sum_of_even_numbers)

# FIZZBUZZ EXERCISE:
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print('FizzBuzz')
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print('Buzz')
#     else:
#         print(number)

# PASSWORD GENERATOR EXERCISE:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                                         'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = 4
nr_numbers = 4
nr_symbols = 4
# nr_symbols = int(input("How many symbols would you like in your password? "))
password = ''

# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
#     print(password)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
#     print(password)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
#     print(password)


def add_letter():
    return random.choice(letters)


def add_number():
    return random.choice(numbers)


def add_symbol():
    return random.choice(symbols)


function_list = [add_letter]*nr_letters + \
    [add_number]*nr_numbers + [add_symbol]*nr_symbols

random.shuffle(function_list)

for function in function_list:
    password += function()

print(password)
