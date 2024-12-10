import pandas
import random

# Exercise 1: Basic Dictionary Comprehension
# Create a dictionary where keys are numbers 1-10 and values are their squares
# Expected output: {1: 1, 2: 4, 3: 9, ...}
numbers_squared = {num: num**2 for num in range(1, 11)}
# print(numbers_squared)


# Exercise 2: Dictionary Comprehension with Conditions
# Create a dictionary of numbers 1-20, but only include numbers divisible by 3
# The values should be these numbers multiplied by 2
# Expected output: {3: 6, 6: 12, 9: 18, ...}
numbers_by_three = {num: num*2 for num in range(1, 21) if num % 3 == 0}
# print(numbers_by_three)


# Exercise 3: Working with Strings and Dictionary Comprehension
countries = ["USA", "UK", "France", "Germany", "Italy"]
capitals = ["Washington", "London", "Paris", "Berlin", "Rome"]
# Create a dictionary where keys are countries and values are:
# - The capital name if the country name is longer than 3 letters
# - "Too Short" if the country name is 3 letters or less
country_capitals = {country: capital if len(country) > 3 else "Too Short" 
                   for country, capital in zip(countries, capitals)}

# print(country_capitals)

# Exercise 4: Working with Pandas
# Create this dictionary first:
student_data = {
    "namee": ["John", "Emma", "Alex", "Sarah", "Michael"],
    "age": [19, 18, 20, 19, 21],
    "math_score": [88, 95, 78, 92, 84],
    "science_score": [92, 88, 85, 94, 89],
    "history_score": [85, 90, 88, 91, 87]
}

# 1. Convert it to a DataFrame  
df = pandas.DataFrame(student_data)
# print(df)
# 2. Create a new dictionary containing:
#    - Keys: Student names
#    - Values: Their average score across all subjects
#    - Only include students with an average score above 88

student_averages = {row.namee: (row.math_score + row.science_score + row.history_score) / 3 
                   for (index, row) in df.iterrows() 
                   if (row.math_score + row.science_score + row.history_score) / 3 > 88}

print(student_averages)

