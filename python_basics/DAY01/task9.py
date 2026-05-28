# Q10
# Take a decimal number as input (like 45.78  ) and output its:
#  • Integer part - 45
#  • Fractional part - 0.78

decimal_num = float(input("Enter a decimal number: "))
integer_part = int(decimal_num)
fractional_part = decimal_num - integer_part
print(f"Integer part: {integer_part}")
print(f"Fractional part: {fractional_part}")

