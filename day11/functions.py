#level 1
# 1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    sum = a+b
    return sum

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    pi = 3.14
    return pi*r**2

'''3. Write a function called add_all_nums which takes arbitrary number of
arguments and sums all the arguments. Check if all the list items are number
types. If not do give a reasonable feedback.'''

def add_all_nums(*n):
    sum =0 
    for i in n :
        sum += i
    return sum
print('addition of all numbers : ', add_all_nums(1,4,5))

'''4. Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) +
32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.'''
def convert_celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f
 
'''5. Write a function called check-season, it takes a month parameter and returns
the season: Autumn, Winter, Spring or Summer.'''
def check_season(month):
    month = month.lower()
    if month in ["september", "october", "november"]:
        return "The season is Autumn"
    elif month in ["december", "january", "february"]:
        return "The season is Winter"
    elif month in ["march", "april", "may"]:
        return "The season is Spring"
    elif month in ["june", "july", "august"]:
        return "The season is Summer"
    else:
        return "Invalid month entered"

month = str(input("Enter month: "))
print(check_season(month))

'''6. Write a function called calculate_slope which return the slope of a linear
equation'''
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)"
    slope = (y2 - y1) / (x2 - x1)
    return slope

'''7. Quadratic equation is calculated as follows: ax2 + bx + c = 0. Write a function
which calculates solution set of a quadratic equation, solve_quadratic_eqn.'''
def solve_quadratic_eqn(a,b,c):
    if a == 0:
     return "Coefficient 'a' cannot be zero."
    d = b **2 - 4*a*c
    root1 = (-b + d **0.5)/2*a
    root2 = (-b - d **0.5)/2*a
    return root1 , root2

'''8. Declare a function named print_list. It takes a list as a parameter and it prints
out each element of the list.'''
lst = [1, 2, 3, 4, 5]
def print_list(lst):
    for item in lst:
        print(item)
print(print_list(lst))

'''9. Declare a function named reverse_list. It takes an array as a parameter and it
returns the reverse of the array (use loops).'''
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr
arr = [1, 2, 3, 4, 5]
print("Reversed list:", reverse_list(arr))

'''10. Declare a function named capitalize_list_items. It takes a list as a parameter
and it returns a capitalized list of items'''
def capitalize_list_items(lst):
    return [item.capitalize() for item in lst]
lst = ['apple', 'banana', 'cherry']
print("Capitalized list:", capitalize_list_items(lst))

'''11. Declare a function named add_item. It takes a list and an item parameters. It
returns a list with the item added at the end.'''
def add_item(lst, item):
    lst.append(item)
    return lst

'''12. Declare a function named remove_item. It takes a list and an item
parameters. It returns a list with the item removed from it.'''
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

'''13. Declare a function named sum_of_numbers. It takes a number parameter and
it adds all the numbers in that range.'''
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

'''14. Declare a function named sum_of_odds. It takes a number parameter and it
adds all the odd numbers in that range.'''
def sum_of_odds(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total

'''15. Declare a function named sum_of_even. It takes a number parameter and it
adds all the even numbers in that - range.'''
def sum_of_even(n):
    total = 0
    for i in range(0, n + 1, 2):
        total += i
    return total

#level 2
'''1. Declare a function named evens_and_odds . It takes a positive integer as
parameter and it counts number of evens and odds in the number.'''
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"Evens: {evens}, Odds: {odds}"

'''2.Call your function factorial, it takes a whole number as a parameter and it
return a factorial of the number'''
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

'''3.Call your function is_empty, it takes a parameter and it checks if it is empty or
not'''
def is_empty(param):
    if param == None:
        return len(param) == 0
    return param == ""

'''4. Write different functions which take lists. They should calculate_mean,
calculate_median, calculate_mode, calculate_range, calculate_variance,
calculate_std (standard deviation).'''

def calculate_mean(lst):
    if len(lst) == 0:
        return "List is empty"
    return sum(lst) / len(lst)  

def calculate_median(lst):
    if len(lst) == 0:
        return "List is empty"
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]
def calculate_mode(lst):
    if len(lst) == 0:
        return "List is empty"
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    return modes
def calculate_range(lst):
    if len(lst) == 0:
        return "List is empty"
    return max(lst) - min(lst)
def calculate_variance(lst):
    if len(lst) == 0:
        return "List is empty"
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst)
def calculate_std(lst):
    if len(lst) == 0:
        return "List is empty"
    variance = calculate_variance(lst)
    return variance ** 0.5

#level 3
# 1. Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#2. Write a functions which checks if all items are unique in the list.
def are_items_unique(lst):
    return len(lst) == len(set(lst))

#3. Write a function which checks if all the items of the list are of the same data type.
def are_items_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(item, first_type) for item in lst)

#4.Write a function which check if provided variable is a valid python variable

'''5. Go to the data folder and access the countries-data.py file.
 Create a function called the most_spoken_languages in the world. It should
return 10 or 20 most spoken languages in the world in descending order
 Create a function called the most_populated_countries. It should return 10 or
20 most populated countries in descending order.'''
countries_data = [
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
def most_spoken_languages(countries_data):
    language_count = {}
    for country in countries_data:
        for language in country['languages']:
            language_count[language] = language_count.get(language, 0) + 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:20]
def most_populated_countries(countries_data):
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:20]