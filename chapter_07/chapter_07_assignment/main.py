from calculations import calculate_pending, get_payment_status, calculate_total_collected, calculate_total_pending, get_pending_students
from students import students
from reports import get_all_student_report, print_report

print(calculate_pending(2,3))
print(get_payment_status(0))
print(calculate_total_collected(students))
print(calculate_total_pending(students))
print(get_pending_students(students))

print(get_all_student_report(students))
print(print_report(students))