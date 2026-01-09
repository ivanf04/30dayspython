#day 7 exercises 
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
additionalCompanies = ('NVIDIA', 'Peet\'s', 'BMW')
it_companies.update(additionalCompanies)
print(it_companies)
it_companies.remove('Peet\'s')
print(it_companies)

# Question 5: Remove throws errors when a nonexistant element is given as an arguement, discard does not have this behavior
# A.update(B)
# print(A)
print(A.intersection(B))
if A.issubset(B):
    print('A is a subset of B')
else:
    print('A is not a subset of B')
if A.isdisjoint(B):
    print('A is a disjoint set of B')
else:
    print('A is not a disjoint of B')
print(A.symmetric_difference(B))

del A
del B

age_set = set(age)
if len(age) > len(age_set):
    print('The age list is longer')
else:
    print('The age set is longer')

# Level 3 question 2: A string is a block of text, characters stored sequentially in memory.
# A lists is an indexed and orders collection of objects. List elements are mutable and individually accessible
# A Tuple is similar to a list, but its elements are immuatble 
# A set is an unodered immutable collection of objects, they operate similarly to sets in mathematics