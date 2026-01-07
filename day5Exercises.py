# # # # list = []
# # # # list2 = [1, 2, 3, 4, 5, 6]
# # # # print(len(list2))
# # # # first = list2[0]
# # # # middle = list2[len(list2) // 2]
# # # # last = list2[-1]
# # # # print(first)
# # # # print(middle)
# # # # print(last)

# # # mixedDataTypes = ['Ivan Faranda', 21, "5\'8\"", False, '1520 Bradford Way']
# # # print(mixedDataTypes)
# # # print(len(mixedDataTypes))
# # # mixedDataTypes[0] = 'Ivan Aranda'
# # # print(mixedDataTypes)
# # # mixedDataTypes.append('Morgan Hill')
# # # print(mixedDataTypes)
# # # mixedDataTypes.insert(len(mixedDataTypes) // 2, "95037")
# # # print(mixedDataTypes)
# # # mixedDataTypes[0] = mixedDataTypes[0].upper()
# # # print(mixedDataTypes)
# # # list = ['#: ']
# # # mixedDataTypes.extend(list)
# # # print(mixedDataTypes) 
# # # exists = False in mixedDataTypes
# # # print(exists)
# # # mixedDataTypes.reverse()
# # # print(mixedDataTypes)
# # # mixedDataTypes.pop(0)
# # # mixedDataTypes.pop(0)
# # # mixedDataTypes.pop(0)
# # # print(mixedDataTypes)
# # # mixedDataTypes.pop(len(mixedDataTypes) // 2)
# # # print(mixedDataTypes)
# # # mixedDataTypes.pop()
# # # print(mixedDataTypes)
# # # mixedDataTypes.clear()
# # # print(mixedDataTypes)
# # # del mixedDataTypes

# # front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# # back_end = ['Node', 'Express', 'MongoDB']

# # full_stack = front_end + back_end
# # print(full_stack)

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# ages.sort()
# print(len(ages))
# ages.append(ages[len(ages) - 1])
# ages.insert(0, ages[0])
# print(ages)
# print(len(ages))
# median = 0
# if len(ages) % 2 != 0:
#     median = ages[len(ages) // 2]
# else: 
#     median = (ages[len(ages) // 2] + ages[(len(ages) // 2) + 1]) / 2

# print(median)
# temp = 0
# for age in ages:
#     temp += age
# mean = temp / len(ages)
# print(mean)
# range = ages[len(ages) - 1] - ages[0]
# print(range)
# min_ave = abs(ages[0] - mean)
# max_ave = ages[len(ages) - 1] - mean
# print(min_ave)
# print(max_ave)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

length = len(countries)
if length % 2 == 0: 
    middleIndex = (length // 2)
else:
    middleIndex = (length // 2) + 1
firstHalf = countries[0:middleIndex]
secondHalf = countries[middleIndex:]
validSplit = False
if len(firstHalf) + len(secondHalf) == length:
    validSplit = True
else: 
    validSplit = False
print(validSplit)

places = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
place1, place2, place3, *rest = places
print(places)
print(place1)
print(place2)
print(place3)
print(rest) 