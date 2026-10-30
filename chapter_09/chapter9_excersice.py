# Exercise 01

print("This is Division calculator")


try:
    num1 = int(input("Enter a Number: "))
    num2 = int(input("Enter Second Number: "))
    answer = num1/num2
    print(answer)
except ValueError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)




# Exercise 02

try:
    file = open("text.txt", "r")
    print(file.read())
except FileNotFoundError as error:
    print(error)
else:
    print("File Opened")
finally:
    print("Programme completed")





# EXercise 03

def get_age(age):
    if age < 0 or age > 100:
        raise ValueError("Age Should be abow 0 and below 100")

try:
    age = int(input("Enter you age: "))
    get_age(age)

except ValueError as error:
    print(error)
else:
    print("Your age is ",age)





# Exercise 04

def fee_collection(pending, paid):
    if paid <= 0 or paid > pending:
        raise ValueError("Unlvalid Amount")
    else:
        return pending - paid


try:
    pending = int(input("Enter Pending Amount: "))
    paid = int(input("Enter Paid Amount: "))

    n_pending = fee_collection(pending, paid)
    print(n_pending)
except ValueError as error:
    print(error)
else:
    print("Action Completed")







# Exercise 05

class InfinityError(Exception):
    pass

try:
    value = int(input("Enter a number"))
    if value < 0:
        raise ValueError("Enter Valid Number")
    elif value > 10000:
        raise InfinityError("Enter Small Amount")
except ValueError as error:
    print(error)
except InfinityError as error:
    print(error)
else:
    print("Programme worked")
finally:
    print("programme Completed")









# Exercise 06

class InsufficientFeeError(Exception):
    pass

try:
    pending = int(input("Enter pending amount: "))
    paid = int(input("Enter paid amount: "))

    if paid > pending:
        raise InsufficientFeeError("Enter payable amount")
except InsufficientFeeError as error:
    print(error)




