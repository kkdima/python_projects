student_heights = [180, 124, 165, 173, 189, 169, 146]

total_height = 0

for x in student_heights:
    total_height += x

total_students = 0

for student in student_heights:
    total_students += 1


average_height = round(total_height / total_students)

print(average_height)
