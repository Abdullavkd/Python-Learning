print("Exercise 01")

students = ["Shamil", "Salman", "Jafar", "Midlaj", "Mujthaba"]

students.append("Misbah")
print(students)
students.pop()
print(students, len(students))







print("Exercise 02")

given_numbers = [10, 20, 10, 30, 20, 40, 30]
sorted_numbers = set(given_numbers)
print(sorted_numbers)





print("Exercise 03")

student_dictionary = {
    "name":"Mifthah", "age":43, "course":"BBA", "paid_fee":13000
}

print(student_dictionary['name'])
print(student_dictionary['age'])
print(student_dictionary['course'])
print(student_dictionary['paid_fee'])

student_dictionary['paid_fee'] = 15000
student_dictionary['city'] = "Calicut"

print(student_dictionary)








print("Exercise 04")

given_text = ' PYTHON backend developer  '
stripped_text = given_text.strip()
print(stripped_text)
lowercased = stripped_text.lower()
print(lowercased)
splitted = lowercased.split()
print(len(splitted))







print("Exercise 05")

students = [
    {"name": "Abdulla", "paid": 15000},
    {"name": "Muhammed", "paid": 8000},
    {"name": "Ali", "paid": 18000}
]


selected_students = [
    student for student in students
    if student['paid']>=10000
]

for name in selected_students:
    print(name['name'])