# day 11 level 2 exercise 2
from collections.abc import Collection

def isEmpty(i):
    if isinstance(i, Collection):
        if i:
            return True
        else:
            return False
    else:
        print('Argument is not an instance of Collection')
        
print(isEmpty([]))
print(isEmpty([1, 2]))
print(isEmpty(4))