numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
# print(new_numbers)

name = "Magda"
letters_list = [letter for letter in name]

double_range = [n*2 for n in range(1,5)]
# print(double_range)

names = ["Alex", "Beth", "Caroline", "Dave","Elenor", "Freddie"]
capital_names = [name.upper() for name in names if len(name)>5]
# print(capital_names)

import random
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

passed_students = {student: score for (student, score) in students_scores.items() if score > 60}
print(passed_students)