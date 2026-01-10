# day 9 exercises 

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive!')
else:
    years_remaining = str(18 - age)
    print("You will be old enough to dirve in " + years_remaining + " years.")

