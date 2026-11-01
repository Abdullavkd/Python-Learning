


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display_details(self):
        return {
            "Name": self.name,
            "Email": self.email,
        }


class Admin(User):
    def __init__(self, name, email, admin_id):
        super().__init__(name, email)
        self.admin_id = admin_id

    def display_details(self):
        print(f"{self.name}, {self.email}, {self.admin_id}")
        
    def manage_students(self, student, action):
        print(f"{self.name} {action} {student}")


class Accountant(User):
    def __init__(self, name, email, bank_account):
        super().__init__(name, email)
        self.bank_account = bank_account

    def display_details(self):
        base_details = super().display_details()
        print(base_details)

    def collect_fee(self, name, amount):
        self.bank_account.deposite(amount)
        print(f"collected fund from {name} amount {amount}")

    def withdraw_dep(self, name, amount):
        self.bank_account.withdraw(amount)
        print(f"Refunded to {name} amount {amount}")

    def dispalay_payment_report(self):
        balance = self.bank_account.get_balance
        print(balance)


class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject

    def display_details(self):
        print(f"{self.name}, {self.email}, {self.subject}")

    def students_information(self, student_name):
        print(f"{self.name} is reviewing {student_name}")  


class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    
    @property
    def get_balance(self):
        return(f"Balance is : {self.__balance}")

    
    def deposite(self, amount):
        if amount < 1:
            raise ValueError("Less than Zero is Not allowed")
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 1 or amount > self.__balance:
            raise ValueError("Enter Valid Amount")
        self.__balance -= amount



school_bank_account = BankAccount(5000)

admin = Admin("Admin", "admin@gmail.com", "ADM-001")
accountant = Accountant("Accountant", "accountant@gmail.com", school_bank_account)
teacher = Teacher("Teacher", "teacher@gmail.com", "Maths")

admin.manage_students("Irshad", "Approved")
accountant.collect_fee("Mufsir", 87348)
accountant.withdraw_dep("Jabir", 90000)

teacher.display_details()
teacher.students_information("Adhil")



admin.display_details()
accountant.display_details()
print(school_bank_account.get_balance)

accountant.dispalay_payment_report()