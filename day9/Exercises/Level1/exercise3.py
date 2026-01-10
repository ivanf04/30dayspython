# day 9 exercise 3

a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))

if (a > b):
    print(str(a) + ' is greater than ' + str(b))
elif (b > a):
    print(str(b) + ' is greater than ' + str(a))
else:
    print(str(a) + ' and ' + str(b) + ' are equal')
    