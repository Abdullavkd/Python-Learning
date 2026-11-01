class Student:
    total_collected = 0
    total_fees = 0
    pending_students = 0

    def __init__(self, name, total_fee, paid):
        self.name = name
        self.total_fee = total_fee
        self.paid = paid
        Student.total_collected+=paid
        Student.total_fees+=total_fee
        if total_fee - paid > 0:
            Student.pending_students +=1
    
    def cal_pending(self):
        return self.total_fee - self.paid
    
    def display_student(self):
        pending = self.cal_pending()
        return {
            "name": self.name,
            "Total Fee": self.total_fee,
            "Paid": self.paid,
            "Pending": pending
        }
    

    @classmethod
    def total_collected_and_pending(cls):
        return {
            "Total Collected": cls.total_collected,
            "total Pending": cls.total_fees - cls.total_collected,
            "Pending Students Count": cls.pending_students
        }
    

student1 = Student("Shamil", 10000, 2000)
student2 = Student("Jabir", 30000, 3000)
student3 = Student("Jumana", 10000, 4000)
student4 = Student("Suhail", 50000, 30000)
student5 = Student("Misal", 90000, 90000)

print(student1.display_student())
print(student2.display_student())
print(student3.display_student())
print(student4.display_student())
print(student5.display_student())


total_report = Student.total_collected_and_pending()
print(total_report)