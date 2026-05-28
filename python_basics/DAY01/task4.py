# Q4
# . The user enters a string containing a number (e.g., "45"). Convert it to:
# • 
# an integer
# • 
# a float
# • 
# a string again
# Print all three values with their types

num_str = input("enter a number")

num_int = int(num_str)
num_float = float(num_str)
num_str_again = str(num_str)

print(f"Integer value: {num_int}, type: {type(num_int)}")
print(f"Float value: {num_float}, type: {type(num_float)}")
print(f"String value: {num_str_again}, type: {type(num_str_again)}")

