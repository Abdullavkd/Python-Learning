# Exercise 01



students = [
    {"name": "Abdulla", "total_fee": 15000, "paid": 15000},
    {"name": "Muhammed", "total_fee": 12000, "paid": 8000},
    {"name": "Ali", "total_fee": 18000, "paid": 18000},
    {"name": "Aisha", "total_fee": 10000, "paid": 0},
    {"name": "Fatima", "total_fee": 14000, "paid": 7000}
]




with open("students.txt", "w") as file:
    for student in students:
        file.write(student["name"] + "\n")


with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())










# Exercise 02

with open("students.txt", "a") as file:
    file.write("Bilal")

with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())






# EXercise 03
import json

one_student = {"name": "Rahima", "total_fee": 14000, "paid": 7000}

with open("student.json", "w", encoding="utf-8") as file:
    json.dump(one_student, file, indent=2)



with open("student.json", "r", encoding="utf-8") as file:
    loaded_student = json.load(file)

    print(loaded_student)




# Exersice 04
json_text = json.dumps(students)
loaded_text = json.loads(json_text)

print(f"{json_text}\n{loaded_text}")






# Exercise 05

import csv

headers = ["name", "total_fee", "paid"]

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)

    writer.writeheader()

    writer.writerows(students)



with open("students.csv", "r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    total_amount_collected = 0

    for row in reader:
        total_amount_collected += int(row["paid"])

    print(f"Total Collected Amount: {total_amount_collected}")













# Exercise 06

try:
    with open("fees.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file is Missing")

except PermissionError:
    print("You have no access to open this file")