# Q9. Write a function 
# is_prime(n) 
# that returns true if n is a prime number and 
# otherwise false, using a loop.

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(2))    
