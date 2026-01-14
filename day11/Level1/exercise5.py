# day 11 level 1 exercise 5

seasons = {
    'Summer' : ('June', 'July', 'August'),
    'Fall' : ('August','September', 'November'),
    'Winter' : ('December', 'January', 'Feburary'),
    'Spring' : ('March', 'April', 'May')
}
def checkSeason(month):
    month = month.capitalize()
    for key in seasons.keys():
        if month in seasons.get(key):
            return key
    else:
        return -1
month = input('Enter a month as a string: ')
print(checkSeason(month))