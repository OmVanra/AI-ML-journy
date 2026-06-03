# Write a program that takes a string from the user and prints the number of 
# spaces in the string

def count_spaces():
    user_input = input("Enter a string: ")
    space_count = user_input.count(' ')
    print(f"The number of spaces in the string is: {space_count}")

print("Welcome to the Space Counter!")
count_spaces()