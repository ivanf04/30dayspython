#exercises for day 6
emptyTuple = ()
brothers = ('Sam', 'Carl', 'Alex')
sisters = ('Jenna', 'Rachelle', 'Abigail')
siblings = brothers + sisters 
print(siblings)
numberOfSiblings = str(len(siblings))
print('I have ' + numberOfSiblings + ' siblings')
parents = ('Father', 'Mother')
familyMembers = parents + siblings
print(familyMembers)

dad, mom, *rest = familyMembers
print(dad)
print(rest)
sibling1, sibling2, sibling3, *rest = rest
print(sibling1)
print(rest)

#after unpacking save "rest" if more unpacking follows

fruits = ('orange', 'apple', 'kiwi', 'mango')
vegetables = ('celery', 'brocoli', 'asaragus')
animalProducts = ('bacon', 'arrachera', 'butter', 'milk')
foodStuff = fruits + vegetables + animalProducts
print(foodStuff)

foodList = list(foodStuff)

#splicing out the middle item from food stuff
length = len(foodStuff)
print(length)
middleIndex = length // 2
if length % 2 == 0: #even number of elements, two middle items
    middleItem = foodStuff[middleIndex -1: middleIndex + 1]
    print(middleItem)
else:   #odd number of elements, only one middle item
    middleItem = foodStuff[middleIndex: middleIndex + 1]
    print(middleItem)
del foodStuff

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
