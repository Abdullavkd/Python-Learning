students = ["Abdulla", "Muhammed", "Ali", "Aisha", "Fatima"]
total_fees = [15000, 12000, 18000, 10000, 14000]
paid_amounts = [15000, 8000, 18000, 0, 7000]


for student, total, paid in zip(students, total_fees, paid_amounts):
    print(f"Student Name: {student}, Total: {total}, Paid: {paid}")



pending = [total_fees[i] - paid_amounts[i] for i in range(len(students))]
print(pending)
    

for num, (student, total, paid, pending) in enumerate(zip(students, total_fees, paid_amounts, pending),start=1):
    if pending <= 0:
        status = "Fully Paid"
    else:
        status = "Payment Pending"
    print(f"{num}. Student Name: {student}, Total: {total}, Paid: {paid}, Pending: {pending}, Status: {status}")




sum = 0
for amount in paid_amounts:
    sum+=amount

print(sum)
