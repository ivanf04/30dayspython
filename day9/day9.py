# Day 9, conditionals
# finally getting to the fun stuff 

#a = 3
# a = 0
# if a > 0:
#     print('A is positive') 
# else:
#     print('A is less than or equal to zero')

# a = 0 
# if a > 0:
#     print('A is positive')
# elif a < 0:
#     print('A is negative')
# else:
#     print('A is positive')

# shorthand 
a = -3
print('A is positive') if a > 0 else print('A is negative')
print()

#you can nest if statements 
#b = 8
b = 9
if b > 0 and b % 2 == 0: 
    print('b is a positive even number')
elif b > 0 and b % 2 != 0:
    print('B is odd and positive')
elif b == 0:
    print('B is zero')
else:
    print('b is negative')

#or is also a logical operator, same as || in java 