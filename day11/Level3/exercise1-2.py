# day 11 level 3 exercise 1 (iterative solution)
import math

def isPrime(n):
    sqrtN = int(math.sqrt(n))
    for i in range(2,sqrtN):
        if n % i == 0:
            return False
    return True

print(isPrime(64))
print(isPrime(191))