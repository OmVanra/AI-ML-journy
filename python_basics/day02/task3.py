# Q3. Write a function that prints the digits of a number, . 
# For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them. 
 
 
# [Hint - The right most digit of a number N is N%10. 
# And to remove the right most digit from a number, we can do N = N / 10.] 



def print_digits(n):
    while n > 0:
        last_digit = n % 10
        print(last_digit)
        n = n // 10 # remove last digit


number = int(input("enter a number to count digit of it."))
print(print_digits(number))