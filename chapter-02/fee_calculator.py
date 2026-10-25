student_name = "Muhammed"
total_fee_text = "15000"
paid_amount_text = "6000"

total_fee = int(total_fee_text)
total_paid = int(paid_amount_text)

pending = total_fee - total_paid
percentage = (total_paid / total_fee) * 100

print(f"Student: {student_name}")
print(f"Total Fee: {total_fee}")
print(f"Paid Amount: {total_paid}")
print(f"Remaining Fee: {pending}")
print(f"Payment Percentage: {percentage}")