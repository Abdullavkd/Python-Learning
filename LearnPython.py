# // Conditional Statements in Python
# // if, elif, and else are used to control the flow of a program based on certain conditions.

a = 10
b = 20
c = 30

# if(a>b):
#     if(a>c):
#         print(a)
#     else:
#         print(c)
# else:
#     if(b>c):
#         print(b)
#     else:
#         print(c)





# if(a>b and a>c):
#     print(a)
# elif(b>a and b>c):
#     print(b)
# else:
#     print(c)











# Loops
# For Loop
# for i in range(from,to,increment or decrement)

# for i in range(1,10):
#     print(i)

# print("Print Even Numbers")
# for i in range(2, 21, 2): # print Even Numbers
#     print(i)

# print("Print Odd Numbers")
# for i in range(1, 20, 2): # Print Odd Numbers
#     print(i)


# print( "Collect Limit From User and Print")
# limit = int(input("Enter Limit to Print: "))

# for i in range(1, limit+1):
#     print(i)


# print("Print Sum of A range")
# start = int(input("Enter Starting Number"))
# end = int(input("Enter Ending Number"))
# sum = 0

# for i in range(start, end+1):
#     sum+=i
# print(sum)


# While Loop
# initialization - a=3;
# while(condition):
    # work

# whileLimit = int(input("Enter Limit: "))
# i=1
# while (i<whileLimit+1):
#     print(i)
#     i+=1




# Pattern Printing
# Star Printing

# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()


# for i in range(9):
#     for j in range(i):
#         print("*",end=" ")
#     print()




# for i in range(6):
#     for j in range(6,i,-1):
#         print("*",end=" ")
#     print()




# for i in range(5):
#     for j in range(5):
#         print(1,end="")
#     print()



# for i in range(5):
#     a=1
#     for i in range(i):
#         print(a,end="")
#         a+=1
#     print()


# for i in range(5):
#     for j in range(i):
#         print(i, end="")
#     print()



# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()


# for i in range(1,6):
#     for j in range(i):
#         print(i,end="")
#     print()


# for i in range(1,6):
#     for j in range(i):
#         print(chr(i+64),end="")
#     print()



# for i in range(1,6):
#     for j in range(i):
#         print(chr(j+65),end="")
#     print()



# for i in range(5,0,-1):
#     for j in range(i):
#         print(chr(j+65),end="")
#     print()



# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end="")

#     for k in range(2*i+1):
#         print("*",end="")

#     print()


# for i in range(5):
#     z=0
#     for j in range(5-i-1):
#         print(" ",end="")
#     for k in range(1,2*i+2):
#         print(z,end="")
#         z+=2
#     print()




# for i in range(5):
#     for j in range(5-i-1):
#         print(" ",end="")

#         val = 1
#     for k in range(i+1):
#         print(val,end="")
#         if k<i:
#             val+=2

#     for k in range(i):
#         val-=2
#         print(val,end="")
#     print()
