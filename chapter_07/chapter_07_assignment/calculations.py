def calculate_pending(total_fee, paid):
    return total_fee - paid


def get_payment_status(pending):
    if pending <= 0:
        return "Fully Paid"
    else:
        return "Payment Pending"



def calculate_total_collected(students):
    total_collected = 0
    for amount in students:
        total_collected += amount['paid']

    return total_collected

# total_collected = calculate_total_collected(students)



def calculate_total_pending(students):
    total_pending = 0
    for amount in students:
        total_pending += (amount['total_fee'] - amount['paid'])

    return total_pending

# total_pending = calculate_total_pending(students)



def get_pending_students(students):
    pending_students = []
    for student in students:
        if student['total_fee'] - student['paid'] > 0:
            pending_students.append(student)

    return pending_students

# pending_students = get_pending_students(students)

