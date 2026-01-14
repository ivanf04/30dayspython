# day 11 level 1 exercise 6
def findSlope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))

# p1 = [2, 3]
# p2 = [3, 5]

p1 = [x1, y1]
p2 = [x2, y2]


print(findSlope(p1, p2))