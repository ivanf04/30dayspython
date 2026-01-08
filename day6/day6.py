#day 6 tuples, review of basic syntax
emptyTuple = ()
#empty tuple using tuple constructor
emptyTuple2 = tuple()

tpl = ('item1', 'item2', 'item3')
fruits = ('apple', 'banana', 'cherry', 'date')
print(fruits)
print(len(fruits))

#indexing is the same as lists
firstFruit = fruits[0]
print(firstFruit)
firstFruitNegativeIndex = fruits[-4]
print(firstFruitNegativeIndex)

#slicing tuples 
allFruits = fruits[:]
print(allFruits)
someFruits = fruits[1:3]
print(someFruits)
allFruitsNegativeIndex = fruits[-4:]
print(allFruitsNegativeIndex)

#changing tuples to lists 
list = list(fruits)
print(list)
list.append('orange')
print(list)
fruits1 = list[0]
print(fruits1)

#checking membership 
print('apple' in fruits)
print('kiwi' in fruits)

#joining tuples 
moreFruits = ('kiwi', 'mango')
allFruits = fruits + moreFruits
print(allFruits)

#deleting tuples
del fruits
# print(fruits) #this will raise an error because the tuple is deleted