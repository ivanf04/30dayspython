# day 11, functions (yay)
# def keyword to define a function

# function with no parameters
def generateFullName():
    firstName = 'Bob'
    lastName = 'Jones'
    fullName = firstName + ' ' + lastName
    print(fullName)
generateFullName()

def addTwoNumbers():
    num1 = 3
    num2 = 5
    total = num1 + num2
    print(total)
addTwoNumbers()

# return keyword is used to return a value 
def addTwoNumsReturn():
    num1 = 5
    num2 = 20
    return (num1 + num2)
print(addTwoNumsReturn())

def greetings (name):
    message = 'Hello ' + name + ' its nice to meet you :)'
    return message
print(greetings('Donte'))

def addTen(num):
    return num + 10
print(addTen(50))

def square(num):
    return num * num
print(square(200))

def areaOfCircle(radius):
    PI = 3.14159
    return PI * (radius ** 2)
print(areaOfCircle(1))

def sumOfNums(num):
    total = 0
    for i in range(num + 1):
        total += i
    return total
print(sumOfNums(100))

def generateFullName(firstName, LastName):
    return firstName + ' ' + LastName
print('Full Name:', generateFullName('Alex', 'Pereira'))
print(generateFullName(LastName= 'Pereira', firstName= 'Alex'))

def sumTwoNums(i, j):
    return i + j
print(sumTwoNums(500, 123441))

def calculateAge(currentYear, birthYear):
    return currentYear - birthYear
print(calculateAge(2026, 1995))

def weightOfObject(mass, gravity= 9.81):
    weight = mass * gravity
    formattedWeight = f'{weight:.3f}'
    return formattedWeight + 'N'
print(weightOfObject(100,9.8))

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(isEven(12))

def findEvenNums(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(findEvenNums(25))

# default parameters when a argument is not passed 
def calculateAge2(birthYear, currentYear= 2026):
    return currentYear - birthYear
print(calculateAge2(1800))

#unknown number of arguments 
def sumAll(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sumAll(1, 2, 3, 4, 5, 6))
print(sumAll(3,4))

def generateTeam(name, *players):
    playerList= []
    for player in players:
        playerList.append(player)
    team = { name : playerList }
    return team
#people = ['Dough', 'Margrett', 'Johnny', 'Sam']
name = 'Tigers' 
print(generateTeam(name, 'Dough', 'Margrett', 'Johnny', 'Sam'))

# unpack dictionary as argument to function
def greet(name, location):
    print(f'Hi {name} from {location} its nice to meet you!')
nameDict = {'name': 'Alice', 'location' : 'Maryland'}
greet(**nameDict)

# function as a parameter
def squareNum2(n):
    return n ** 2
def doSomething(f ,x):
    return f(x)
print(doSomething(squareNum2, 3))
