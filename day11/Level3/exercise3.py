# day 11 level 3 exercise 3

def checkType(items):
    dataType = type(items[0])
    for item in items:
        if not isinstance(item, dataType):
            return False 
    return True

print(checkType([1,2,3,4]))
print(checkType([1,2,3,4.5]))