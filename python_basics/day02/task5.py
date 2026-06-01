# Q5. Write a function to return the sum of digits of a number, . 


def sum_of_digits(n):
    result = 0
    for i in range(1,n+1):
        result += i
    print("result:",result)

sum_of_digits(4)    