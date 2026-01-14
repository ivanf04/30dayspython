# day 11 level 1 exercise 7
import math
def solveQuadratic(a, b, c):
    positive =  ((b * -1) + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    negative =  ((b * -1) - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    return [positive, negative]

print(solveQuadratic(1, 5, 6))