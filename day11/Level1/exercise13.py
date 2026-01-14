# day 11 level 1 exercise 13

def sumOfNUms(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total

print(sumOfNUms(4))