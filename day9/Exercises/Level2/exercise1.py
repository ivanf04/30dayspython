#day 9 exercises, level 2 question 1

grade = float(input('Enter your grade: '))

if(100 >= grade and grade >= 90):
    print('A')
elif (89 >= grade and grade >= 80):
    print('B')
elif (79 >= grade and grade >= 70):
    print('C')
elif(69 >= grade and grade >= 60):
    print('D')
else:
    print('F')

