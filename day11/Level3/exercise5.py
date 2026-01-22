# day 11 level 3 exercise 5
import countries_data
countryList = countries_data.counrtyList

def topLanguages(countries):
    languages = {}
    for country in countries:
        for language in country['languages']:
            if(language not in languages):
                languages[language] = 1
        else:
            languages[language] += 1
    sortedLanguages = sorted(languages.items(), key=lambda item: item[1], reverse=True) 
    return sortedLanguages[:10]
    
def topCountries(countries):
    populations = {}
    for country in countries:
        populations[country['name']] = country['population']
    sortedPopulations = sorted(populations.items(), key=lambda item: item[1], reverse=True)
    return sortedPopulations[:10]

print(f'{topLanguages(countryList)}\n\n{topCountries(countryList)}')
