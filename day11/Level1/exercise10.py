# day 11 level 1 exercise 10 

def capitalizeItems(items):
    for i in range(len(items)):
        items[i] = items[i].capitalize()
    return items
list = ['dog', 'cat', 'bird']
list = capitalizeItems(list)
print(list)
