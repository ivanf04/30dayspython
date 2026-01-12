# day 10 level 3 exercise 3
import countries_data
countryList = countries_data.counrtyList

#numberOfLanguages = 0
languages = {}
populations = {}
for country in countryList:
    for language in country['languages']:
        if(language not in languages):
            languages[language] = 1
        else:
            languages[language] += 1
    populations[country['name']] = country['population']

print(f'{len(languages)} are spoken in the world')
print('Here are the top ten most spoken languages.')
sortedLanguages = sorted(languages.items(), key=lambda item: item[1], reverse=True)
for i in range(10):
    print(sortedLanguages[i])
print()
print('Here are the top ten most populous countries')
sortedPops = sorted(populations.items(), key=lambda item: item[1], reverse=True)
for i in range(10):
    print(sortedPops[i])