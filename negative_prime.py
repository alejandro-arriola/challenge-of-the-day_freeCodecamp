** start of main.py **

import math

def is_unnatural_prime(n):
    return is_prime(-n if n < 0 else n)

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

print(is_prime(5))

** end of main.py **

