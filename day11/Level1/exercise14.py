# day 11 level 1 exercise 14

def sumOfOdds(num):
    total = 0
    for i in range(1, num + 1, 2):
        total += i
    return total 
print(sumOfOdds(5))
print(sumOfOdds(100))