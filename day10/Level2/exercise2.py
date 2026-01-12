# day 10 level 2 exercise 2

odd_sum = 0;
even_sum = 0;
for i in range(101):
    if i % 2 == 0: 
        even_sum += i
    else:
        odd_sum += i
print(f'The sum of all evens in {even_sum}')
print(f'The sum of all odds is {odd_sum}')
