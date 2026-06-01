# Q4. Write a function to return the count the number of digits in a number, . 


def cout_no_of_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count    

result = cout_no_of_digits(1234)
print("number of digit is:",result)        