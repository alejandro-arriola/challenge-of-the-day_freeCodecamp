import math

def is_circular_prime(n):
    def isPrime(n):
        limit = int(math.sqrt(n)) + 1
        for v in range(2, limit, 2):
            if n % v == 0:
                return False
                
        return True   

    for _ in range(len(str(n))):
        if not isPrime(n):
            return False
        n = int(str(n)[1:] + str(n)[0])
    
    return True

print(is_circular_prime(197))