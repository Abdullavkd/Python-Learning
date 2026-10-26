# Exercise 01

def greeting(name):
    return(f"Hello, {name}")

greeting("Muhammed")
greeting("Shamil")





# Exercise 02

def calculate(a, b, operation):
    if operation == "/" and b == 0:
        return print("Divition with Zero is Impossible")
    elif operation == "+":
        return print(a+b)
    elif operation == "-":
        return print(a-b)
    elif operation == "*":
        return print(a*b)
    elif operation == "/":
        return print(a//b)

calculate(7,4,"/")







# Exercise 03

def calculate_pending(total_fee, paid):
    return(total_fee - paid)

calculate_pending(15000, 8000)
calculate_pending(10000, 10000)




# Exercise 04

def introduce(name, role = "Student"):
    return(f"{name} is a {role}")

introduce("Midlaj")
introduce("Ismayeel", "Teacher")




# Exercise 05

def analyze_numbers(numbers):
    if len(numbers) < 1 :
        print("List is Empty")
    else:
        min_number = min(numbers)
        max_number = max(numbers)
        sum_numbers = sum(numbers)

        return min_number,max_number, sum_numbers

minimum , maximum, sum_numbers = analyze_numbers([10, 5, 20, 15])




# Exercise 06

def list_total(numbers):
    return sum(numbers)

total_value = list_total([3,4,5,6])
print(total_value)