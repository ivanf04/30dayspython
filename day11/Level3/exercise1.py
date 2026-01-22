# day 11 level 3 exercise 1
import math

def isPrime(num):
    if num == 1:
        return False
    if num > 2 and num % 2 == 0:
        return False
    else:
        return isPrimeHelper(num, 2)

def isPrimeHelper(n, d):
    if d ** 2 > n:
        return True
    if n % d == 0:
        return False
    else:
        return isPrimeHelper(n, d + 1)
    
print(isPrime(69))
print(isPrime(191))
