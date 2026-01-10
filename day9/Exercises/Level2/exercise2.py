#day 9, level 2 exercise 2

month = input('Enter the month as a string: ')
month = month.capitalize()

seasons = {
    'Autumn' : ('September', 'October', 'November'),
    'Winter' : ('December', 'January', 'February'),
    'Spring' : ('March', 'April', 'May'),
    'Summer' : ('June', 'July', 'August')
}

season = str()

if (month in seasons.get('Autumn')):
    season = 'Autum'
elif (month in seasons.get('Winter')):
    season = 'Winter'
elif (month in seasons.get('Spring')):
    season = 'Spring'
else:
    season = 'Summer'

print('The season is ' + season)