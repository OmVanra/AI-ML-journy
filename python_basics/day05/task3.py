# Q3.
# Create a program that:
# 1. Has a list of numbers: 
# [5, 10, 15, 20, 25]
# 2. Uses a list comprehension to create a new list with only numbers greater 
# than 15
# 3. Prints the new list

numbers = [5, 10, 15, 20, 25]

# Using list comprehension to filter numbers greater than 15
filtered_numbers = [num for num in numbers if num > 15]

# Print the new list
print(filtered_numbers)

