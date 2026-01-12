# day 10 level 3 exercise 3 

fruits = ['banana', 'orange', 'mango', 'lemon']
j = len(fruits) - 1
for i in range(0,2):
    temp = fruits[i]
    fruits[i] = fruits[j]
    fruits[j] = temp
    j -= 1

print(fruits)