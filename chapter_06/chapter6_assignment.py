students = [
    {"name": "Abdulla", "total_fee": 15000, "paid": 15000},
    {"name": "Muhammed", "total_fee": 12000, "paid": 8000},
    {"name": "Ali", "total_fee": 18000, "paid": 18000},
    {"name": "Aisha", "total_fee": 10000, "paid": 0},
    {"name": "Fatima", "total_fee": 14000, "paid": 7000}
]



def calculate_pending(total_fee, paid):
    return total_fee - paid


def get_payment_status(pending):
    if pending <= 0:
        return "Fully Paid"
    else:
        return "Payment Pending"



def get_student_report(student):

    pending = calculate_pending(student['total_fee'], student['paid'])
    status = get_payment_status(pending)
    return {
        "name": student['name'],
        "total_fee": student['total_fee'],
        "paid": student['paid'],
        "pending_amount": pending,
        "status": status
    }






def calculate_total_collected(students):
    total_collected = 0
    for amount in students:
        total_collected += amount['paid']

    return total_collected

total_collected = calculate_total_collected(students)



def calculate_total_pending(students):
    total_pending = 0
    for amount in students:
        total_pending += (amount['total_fee'] - amount['paid'])

    return total_pending

total_pending = calculate_total_pending(students)



def get_pending_students(students):
    pending_students = []
    for student in students:
        if student['total_fee'] - student['paid'] > 0:
            pending_students.append(student)

    return pending_students

pending_students = get_pending_students(students)





def get_all_student_report(students):

    all_student_report = []

    for student in students:

        pending = calculate_pending(student['total_fee'], student['paid'])
        status = get_payment_status(pending)
        all_student_report.append({
            "name": student['name'],
            "total_fee": student['total_fee'],
            "paid": student['paid'],
            "pending_amount": pending,
            "status": status
        })

    return all_student_report


print(get_all_student_report(students))


def print_report(students):
    all_student_report = []
    for student in students:
        print(get_student_report(student))
        all_student_report.append(get_student_report(student))
    return all_student_report


print_report(students)

print(f"Total Fee Collected: {total_collected}")
print(f"Total Fee Pending: {total_pending}")
print(f"Students With Pending fee: {len(pending_students)}")