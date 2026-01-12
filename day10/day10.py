#day 10 loops 
#while and for loops like java 

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

#break and continue statements are similar to java. I wont use them because they are bad practice

#for loops similar to java 
# for loop on a list 
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# for loop on a string 
language = 'Python'
for letter in language:
    print(letter, end='')
print()
for i in range(len(language)):
    print(language[i], end='')
print()

#for loop on a tuple 
numbers2 = (0, 1, 2, 3, 4, 5)
for number in numbers2:
    print(number, end='')
print()

# for loop on a dictionary 
person = {
    'first_name' : 'Cody',
    'Last_name' : 'Garfield',
    'age' : 13,
    'is_married' : False,
    'skills' : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
}
for key in person:
    print(key, end=' ')
print()
for key in person:
    print(person[key], end=' ')
print()

#for loop in a set 
companies = {'Facebook', 'Google', 'Apple', 'Microsoft', 'Oracle'}
for company in companies:
    print(company, end=' ')
print()

# range function =, range(start, end , step)
for number in range(11):
    print(number, end=' ')
print()

#nested loop 
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill, end=' ')
print()

#for else, executes a statement after the for loop 
for number in range(0,12,2):
    print(number, end='')
else:
    print()
    print('The loop has ended')

#use pass operator as a place holder for empty loop body 
for number in range(6):
    pass