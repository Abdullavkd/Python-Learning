class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_detials(self):
        return f"Name is : {self.name}, Email id is : {self.email}"
        

class Admin(User):
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Teacher(User):
    def init(self, name, email):
            self.name = name
            self.email = email


class Accountant(User):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department

    def display_detials(self):
        details = super().display_detials()
        return f"{details}, Department Is : {self.department}"
    
accountant = Accountant("Alex", "alex@school.com", "Finance & Payroll")

print(accountant.display_detials())



class Teacher:
    pass
    
class Principal(Teacher, Accountant):
    pass


class BankAcoount:
    def __init__(self, balance):
        self.__balance = balance
    
    def change_balance(self, amount):
        self.__balance = amount
    
    def get_balance(self):
        return self.__balance

person = BankAcoount(34)
print(person.get_balance())
person2 = person.change_balance(3445)
print(person.get_balance())








class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 1 or value > 100:
            raise ValueError("Enter Valid Age")

        self._age = value

try:
    new_one = Student("Rafal", 10)
    print(new_one.age)

    new_one.age = 121
    print(new_one.age)
except ValueError as error:
    print(error)






class EmailNotification:
    def send(self, message):
        print(message)


class SMSNotification:
    def send(self, message):
        print(message)

class WhatsAppNotification:
    def send(self, message):
        print(message)


SMS = SMSNotification()
Email = EmailNotification()
Whatsapp = WhatsAppNotification()

notifications = [SMS, Email, Whatsapp]

for notification in notifications:
    notification.send("Your Notification is 938493")