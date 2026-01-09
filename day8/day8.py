#day 8, dictionaries 
#dictionaries are similar to HashMap in java 

person = {
    'first_name' : 'Ivan',
    'last_name' : 'Faranda',
    'age' : 250,
    'country' : 'Peru',
    'is_married' : False,
    'skills' : ['management', 'Java', 'React', 'SQL'],
    'address' : {
        'street' : 'street_name',
        'zipcode' : '12345'
    }
}

#values in a dictionary can be any data type, you can store a dictionary within a dictionary

print(len(person))
#access items by key 
print(person['first_name'])
print(person['last_name'])
print(person['skills']) #prints every element of the nested dictionary
print(person['skills'][0])  #specify index of nested dictionary 
# attempting to access an element that does not exist in the dictionary will raise an error 
# use .get() method to prevent this error 
print('access elements using .get()')
print(person.get('first_name'))
print(person.get('skills')[0])
print(person.get('city'))

#adding new key pair to dictionary 
person['job_title'] = 'student'
person['skills'].append('Python')
print(person)

#modifying esixting elements in a dictionary
person['first_name'] = 'Marco'
person['age'] = 5000
print(person.get('first_name') + ' ' + str(person.get('age')))

#use in operator to check if a key exists in a dictionary
print('job_title' in person)
print('SSN' in person)

#Remove elements from a dictionary using pop(), popitem(), and del
print(person.pop('first_name'))     # pop() returns the item being removes 
person.popitem()    #removes the last item from the dictionary
del person['is_married']    #del does not return anyhting, only removes the item
print(person)

# .items function turns a dictionary to a list of tuples 
print(person.items())

#use .clear to clear all items from a dictionary 
#person.clear()
#print(person)

#use del to completely delete a dictionary 
#del person

#use .copy to make a copy of a dictionary 
person_copy = person.copy()
person.clear()
print(person_copy)
print(person)

#.keys() method returns a the keys of a dictionary as a list 
keys = person_copy.keys()
print(keys)

#.values() returns the values of a dictionary as a list 
values = person_copy.values()
print(values)
