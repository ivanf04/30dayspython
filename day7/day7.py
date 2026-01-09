# day 7, sets 
#sets in python are similar to sets in mathematics. You can find union, intersection, difference, ect. 

# st = set()
# st2 = {'item1', 'item2', 'item3'}
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))

#use loops to access item, to be discussed in loop section 

#checking for an item
print('mango' in fruits)
print('kiwi' in fruits)

#items cannot be changed, but we can add items to a set 
fruits.add('kiwi')
print('kiwi' in fruits)
#use update() to add multiple items to a set, update() takes a list argument
veggies = ('tomato', 'lettuce', 'brocolli')
fruits.update(veggies)
print(fruits)
print('tomato' in fruits)

# to remove an item from the set use remove(), calling remove on an element that doesnt exist in the set will raise an error
#discard() method removes an element without raising errors
#pop() removes a random element and returns it 
print('tomato' in fruits)
fruits.remove('tomato')
print('tomato' in fruits)

popped = fruits.pop()
print(popped)
print(popped in fruits)

#use clear() method to empty a set 
fruits.clear()
print(fruits)

#use del operator to delete a set 
#del fruits 

#converting a list to a set, duplicates are removed 
cities = ('San Francisco', 'Los Angeles', 'New York', 'London', 'Lima', 'Lima')
print(cities)
cities = set(cities)
print(cities)

#join sets using the union or update method 
countries = {'United States', 'United Kingdom', 'Peru', 'Mexico'}
# citiesCountries = cities.union(countries)
cities.update(countries)
print(cities)

#Finding intersection, intersection() doesn't modify the sets, returns a new set 
integers = {0, 1, 2, 3, 4, 5, 6}
evenInt = {0, 2, 4, 6}
print(integers.intersection(evenInt))

#subset and superset
print(evenInt.issubset(integers))
print(integers.issuperset(evenInt))

#checking difference between two sets 
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1))
print(st1.difference(st2))

#there are functions for summetric difference and finding disjoint sets
