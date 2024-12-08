# # Create a list of squares for numbers from 0 to 9
# squares = [x**2 for x in range(10)]
# print(squares)

# # Create a list of only the even numbers from 1 to 10
# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)

# # Capitalize each word in a list
# words = ['hello', 'world', 'python']
# capitalized_words = [word.capitalize() for word in words]
# print(capitalized_words)

# # Create a list of numbers from 0 to 29 that are divisible by both 3 and 2
# list_numbers = [x for x in range(31) if x % 3 == 0 and x % 2 == 0]
# print(list_numbers)

# sentence = "The quick brown fox jumps"
# my_list = [x[0] for x in sentence.split()]
# print(my_list)


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)

