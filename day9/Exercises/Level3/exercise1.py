# day 9, level 3 exercise 1

person={
    'first_name': 'Sam',
    'last_name': 'Rosco',
    'age': 250,
    'country': 'Canada',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


if ('skills' in person):
    middle_skill = person['skills'][len(person['skills']) // 2]
    print(middle_skill)
    has_python = 'Python' in person['skills']
    if(has_python):
        print(has_python)
        
front_end = ['JavaScript', 'React']
back_end = ['Node', 'MongoDB', 'Python']

if(front_end == person.get('skills')):
    print('He is a front end developer')
elif(back_end == person.get('skills')):
    print('He is a Backend developer')
else:
    print('He is a full stack developer')

if(person.get('is_married') and person['country'] == 'Canada'):
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married.')

