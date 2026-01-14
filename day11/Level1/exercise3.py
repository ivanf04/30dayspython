# day 11 level 1 exercise 3
def addAllNums(*nums):
    total = 0
    for num in nums:
        if isinstance(num, int):
            total += num
        else:
            print('Arguments must be of type int')
            return -1
    return total
print(addAllNums(1,4,5,6,8,9))
print(addAllNums(1,4,5,6,8,'dog'))