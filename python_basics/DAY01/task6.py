# Q7
# . Ask the user for a temperature in Celsius (string input). Convert it to , float
# then calculate and print temperature in Fahrenheit using the formula: F = (C * 9/5) + 32. Print the result with its type.


temp = input("Enter the temperature in Celsius: ")
temp_float = float(temp)
temp_fahrenheit = (temp_float * 9/5) + 32
print(f"Temperature in Fahrenheit: {temp_fahrenheit}, type: {type(temp_fahrenheit)}")