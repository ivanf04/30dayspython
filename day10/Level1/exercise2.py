#day 10 level 1 exercise 2

for number in range(10, -1, -1):
    print(number, end=' ')
print()

# use else to print a new line at the end, if the loop never executes, the new line will not be printed
count = 10
while (count > -1):
    print(count, end=' ')
    count = count - 1
else:
    print()
