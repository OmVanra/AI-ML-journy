# Q1
# . Ask the user for a string and check whether it is a palindrome or not. 
# A  
# palindrome
# “madam”, “
# is a string which is same when we read it forward & backward. Eg - 
# racecar” etc

def is_palindrome():
    user_input = input("Enter a string: ")
    if user_input == user_input[::-1]:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")

print("Welcome to the Palindrome Checker!")
is_palindrome()

