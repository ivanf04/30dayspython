#Exercises, day 8 
dog = {}
dog['name'] = 'Benny'
dog['color'] = 'Black'
dog['breed'] = 'Lab pitbull mix'
dog['legs'] = 4
dog['age'] = 2

student = {
    'first_name' : 'Bob',
    'last_name' : 'Jenkins',
    'gender' : 'Male',
    'age' : 20 ,
    'is_married' : False,
    'skills' : ['Accounting','Finance', 'Spanish'],
    'country' : 'USA',
    'city' : 'Los Angeles',
    'address' : '123 ABC street'
}

print(len(student))
skills = student.get('skills')
print(skills)
print(isinstance(skills, list))
student['skills'].append('Communication')
print(student.get('skills'))
print()

keys_as_list = student.keys()
print(keys_as_list)
print()

values_as_list = student.values()
print(values_as_list)
print()

tuples = student.items()
print(tuples)
print()

student.pop('is_married')
print(student)
print()

del student