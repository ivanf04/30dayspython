# day 11 level 1 exercise 15

def sumOfEvens(num):
    total = 0
    for i in range(0 , num + 1, 2):
        total += i
    return total
print(sumOfEvens(5))
print(sumOfEvens(100))