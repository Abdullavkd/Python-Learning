from students import students
from calculations import get_payment_status, calculate_pending



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



# print(get_all_student_report(students))


def print_report(students):
    all_student_report = []
    for student in students:
        print(get_student_report(student))
        all_student_report.append(get_student_report(student))
    return all_student_report


# print_report(students)



