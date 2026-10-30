students = [
    {"name": "Abdulla", "total_fee": 15000, "paid": 15000},
    {"name": "Muhammed", "total_fee": 12000, "paid": 8000},
    {"name": "Ali", "total_fee": 18000, "paid": 18000},
    {"name": "Aisha", "total_fee": 10000, "paid": 0},
    {"name": "Fatima", "total_fee": 14000, "paid": 7000}
]



for student in students:
    student["pending"] = student["total_fee"] - student["paid"]
    if student["pending"] <= 0:
        student["status"] = "Fully Paid"
    else:
        student["status"] = "Payment Pending"  

print(students)


import json

with open("fee_report.json", "w", encoding="utf-8") as json_file:
    json.dump(students, json_file, indent=2)


import csv

headers = ["name", "total_fee", "paid", "pending", "status"]
with open("fee_report.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=headers)

    writer.writeheader()
    writer.writerows(students)




with open("fee_report.json", "r", encoding="utf-8") as json_file:
    loaded_text = json.load(json_file)
    print(f"Number of Students Records: {len(loaded_text)}")







with open("fee_report.csv", "r", newline="", encoding="utf-8") as csv_file:
    reader = csv.DictReader(csv_file)

    collected_fee = 0
    for row in reader:
        collected_fee += int(row["paid"])

    print("Total Collected:",collected_fee)




try:
    with open("calicut.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("File Not Found")

except PermissionError:
    print("You dont have permission to open this file")