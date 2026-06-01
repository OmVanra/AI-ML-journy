# Q7. Design a program to continuously input a number from user & print if it is 
# positive or negative until the user enters “Quit”. 

while True:
    number = int(input("Enter a number to check is it positive or negative:"))

    if (number > 0):
        print("positive")
    else:
        print("negative")

    ask = input("Enter 'Quit' for quit ")
    if (ask == 'Quit'):
        break
            