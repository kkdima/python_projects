# import random

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# student_scores = {student: random.randint(1, 100) for student in names}
# print(student_scores)

# passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)

# import string
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word.lower().strip(string.punctuation): len(word.strip(string.punctuation)) for word in sentence.split()}
# print(result)


# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
# weather_f = {day: (degrees * 9/5) + 32 for (day, degrees) in weather_c.items()}
# print(weather_f)


import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
