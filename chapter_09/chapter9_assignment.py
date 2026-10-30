
class InvalidPaymentAmounts(Exception):
    pass


try:
    student_name = input("Enter Student Name: ")
    total_fee = int(input("Total Fee: "))
    paid = int(input("Paid Amount: "))
    
    if total_fee < 0 or paid < 0:
        raise InvalidPaymentAmounts("Negative Numbers are Disabled")
    elif paid > total_fee:
        raise InvalidPaymentAmounts("Paid Amount Should be less than or equal to Total Fee")
    
    pending_amount = total_fee - paid
    print("Pendig Amount: ",pending_amount)
except ValueError as error:
        print(error)
except InvalidPaymentAmounts as error:
    print(error)
except:
    print("Something went wrong")
finally: 
    print("Completed")