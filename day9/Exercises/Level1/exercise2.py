#day 9 exercises question 2

my_age = 21
user_age = int(input("Enter your age: "))

difference = my_age - user_age 

#ugly if branching
if difference > 0:
    if difference == 1:
        print('I am one year older than you')
    else:
        print('I am ' + str(difference) + ' years older than you.')
elif difference < 0:
    difference = abs(difference)
    if difference == 1:
        print('You are 1 year older than me.')
    else:
        print('You are ' + str(difference) + ' years older than me.')
else:
    print('We are the same age.')