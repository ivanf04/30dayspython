# day 11 level 3 exercise 2

def uniqueCheck(items):
    while(items):
        item = items.pop()
        if item in items:
            return False
    return True 

print(uniqueCheck([1,1,2,3,4]))
print(uniqueCheck([1,2,3,4]))
      