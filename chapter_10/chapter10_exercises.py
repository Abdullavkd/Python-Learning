# Excercise 01


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
    

student1 = Student("Muhammed", 45, "Islamic Studies")
print(student1)




# Exercise 02

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    
    def deposte():

    def withdraw():

    



# Exercise 03

class Student:
    def __init__(self, total_fee, paid):
        self.total_fee = total_fee
        self.paid = paid

    def calc_pending(self):
        return self.total_fee - self.paid


student3 = Student(3000, 400)
print(student3.calc_pending())






# Exercise 04

class Employee:
    company = "Ainul Huda Kappad"

    def __init__(self, name):
        self.name = name

student4 = Employee("Muhammed")
student5 = Employee("Muhammed")

print(student4.company)
print(student5.company)




# Exercise 05

class Calculator:
    @staticmethod
    def addition(num1, num2):
        return num1 + num2

    def substraction(num1, num2):
        return num1-num2


value1 = Calculator.addition(34,54)
value2 = Calculator.substraction(84,34)
print(value1, value2)





# Exercise 06

class School:
    school_name = "Ilahiya kappad"
    @classmethod
    def change_school(cls, name):
        cls.school_name = name
        return cls.school_name

school1 = School.change_school("IASC Cheliya")
school2 = School.change_school("IHSS Kappad")
print(school1, school2)