#1. Declare an empty list
list = []

#2. Declare a list with more than 5 items
list =['t1', 't2', 't3', 't4', 't5', 't6']

#3. Find the length of your list
print(len(list))

#4. Get the first item, the middle item and the last item of the list
print("First item:", list[0])
middle_index = len(list) // 2
print("Middle item:", list[middle_index])
print("Last item:", list[-1])

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['pankaj', 18, 5.9, 'Single', 'india']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print("Number of companies:", len(it_companies))

#9. Print the first, middle and last company
print("First company:", it_companies[0])
middle_index = len(it_companies) // 2
print("Middle company:", it_companies[middle_index])
print("Last company:", it_companies[-1])

#10. Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print("Modified companies list:", it_companies)

#11.Add an IT company to it_companies
it_companies.append('Tesla')
print("After adding Tesla:", it_companies)

#12. Insert an IT company at the beginning of the it_companies list
it_companies.insert(0, 'Nvidia')
print("After inserting Nvidia at the beginning:", it_companies)

#13. Change one of the it_companies to uppercase
it_companies[1] = it_companies[1].upper()
print("After changing Microsoft to uppercase:", it_companies)

#14. Join the it_companies with a string '#; '
print( '#; '.join(it_companies))

#15. Check if a certain company exists in the it_companies list
print( 'Google' in it_companies)

#16. Sort the it_companies list
it_companies.sort()
print("Sorted companies list:", it_companies)

#17. Reverse the list in descending order using reverse() method
print(it_companies.reverse())

#18. Slice out the first 3 companies from the it_companies list
print(it_companies[:3])

#19. Slice out the last 3 companies from the it_companies list
print(it_companies[3:])

#20. Slice out the middle IT company or companies from the it_companies list
print(it_companies[4:5])

#21. Remove the first IT company from the it_companies list
print(it_companies.pop(0))

#22. Remove the middle IT company from the it_companies list
print(it_companies.pop(3))

#23. Remove the last IT company from the it_companies list
print(it_companies.pop())

#24. Remove all IT companies from the list
print(it_companies.clear())

#25. Destroy the IT companies list
del it_companies

#26. Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end

#27.After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

#level 2
#1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#Sort the list and find the min and max age
print(ages.sort())
print(ages)
print("Minimum age:", min(ages))
print("Maximum age:", max(ages))

#Add the min age and max age to the list
ages.append(min(ages))
ages.append(max(ages))
print(ages)

#Find the median age (one middle item or two middle items divided by two)
ages = [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
ages.sort()
n = len(ages)
median = (ages[(n-1)//2] + ages[n//2]) / 2

print("Median age:", median)

#Find the average age (sum of all items divided by number of items)
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

#Find the range of the ages (max minus min)
age_range = max(ages) - min(ages)   
print("Range of ages:", age_range)

#Compare the value of (min - average) and (max - average), use abs() method
min_average = abs(min(ages) - average_age)
max_average = abs(max(ages) - average_age)
print("Min - Average:", min_average)
print("Max - Average:", max_average)

#1. Find the middle country(ies) in the countries list
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
middle_country = countries[len(countries) // 2]
print(middle_country)

#2. Divide the countries list into two equal lists if it is even if not one more country for the first half.
half_index = (len(countries) + 1) // 2
first_half = countries[:half_index]
second_half = countries[half_index:]
print("First half:", first_half)
print("Second half:", second_half)

#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country , second_country, third_country, *scandic_countries = country
print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Scandic countries:", scandic_countries)





