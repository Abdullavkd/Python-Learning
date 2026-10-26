students = [
    {"name": "Abdulla", "total_fee": 15000, "paid": 15000},
    {"name": "Muhammed", "total_fee": 12000, "paid": 8000},
    {"name": "Ali", "total_fee": 18000, "paid": 18000},
    {"name": "Aisha", "total_fee": 10000, "paid": 0},
    {"name": "Fatima", "total_fee": 14000, "paid": 7000}
]



print("STUDENT FEE REPORT")

pendings = []

for student in students:
    print(student['name'])
    print(student['total_fee'])
    print(student['paid'])
    pending = student['total_fee']-student['paid']
    print(pending)
    pendings.append(pending)
    if pending == 0 :
        print("Fully Paid")
    else:
        print("Payment Pending")


for student, pending in zip(students, pendings):
    print(f"{student['name']}: {pending}")




total_collected = 0
for amount in students:
    total_collected+=amount['paid']

print(f"total collected amount: {total_collected}")
print(f"total students: {len(students)}")

pending_students_count = 0
for i in pendings:
    if i >= 1:
        pending_students_count+=1


print(f"pending students count is: {pending_students_count}")
