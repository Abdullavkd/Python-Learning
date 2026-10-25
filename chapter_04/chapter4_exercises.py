print("Exercise 01")

for i in range(20):
    if not i % 2 == 0:
        print(i)





print("EXercise 02")

students = ["Muhammed", "Shahal", "Salman", "Jabbar", "Jumailath"]

for index, student in enumerate(students, start=1):
    print(f"{index}. {student}")






print("Exercise 03")

amounts = [983,483,983,3084,388]

for student, amount in zip(students, amounts):
    print(f"{student}: {amount}")





print("Exercise 04")

search_student = "Muhammed"

for student in students:
    if search_student == student:
        print("Student found")
        break
else:
    print("Student not found")






print("Exercise 05")

amounts = [1000, 2500, 0, 1500, 0]
sum = 0

for i in amounts:
    if i == 0:
        continue
    else:
        sum += i

print(sum)