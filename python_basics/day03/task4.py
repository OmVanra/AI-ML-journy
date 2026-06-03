# Q4
# . Given a tuple of integers, create:
# • 
# A tuple of all even numbers
# • 
# A tuple of all odd numbers

def separate_even_odd_numbers(input_tuple):
    even_numbers = tuple(x for x in input_tuple if x % 2 == 0)
    odd_numbers = tuple(x for x in input_tuple if x % 2 != 0)
    return even_numbers, odd_numbers
# Example usage
input_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_tuple, odd_tuple = separate_even_odd_numbers(input_tuple)
print(f"Even numbers: {even_tuple}")
print(f"Odd numbers: {odd_tuple}")
