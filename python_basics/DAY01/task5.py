# Q5 Write a program to  
# swap
# values of two numbers entered by the user.


a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

# Swapping the values

temp = a
a = b
b = temp
print(f"After swapping: a = {a}, b = {b}")