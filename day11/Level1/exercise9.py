# day 11 level 1 exercise 9

def reverseList(list):
    i = len(list)
    newList = []
    while i != 0:
        newList.append(i)
        i -= 1
    return(newList)

list = [1, 2, 3, 4, 5, 6]
print(reverseList(list))