from mypackage import arithmatic
print(arithmatic.add_num(1,4,5,5))

from mypackage import greet
print(greet.greet_person("pankaj" , "behera"))

'''2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and
find :
i. the min, max, mean, median, standard deviation of cats' weight in
metric units.
ii. the min, max, mean, median, standard deviation of cats' lifespan in
years.
iii. Create a frequency table of country and breed of cats'''

import requests
import statistics
import pandas as pd


url = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url)
cats = response.json()


weights = []
lifespans = []
countries = []
breeds = []

for cat in cats:
  
    try:
        weight_range = cat['weight']['metric'].split(' - ')
        weight_avg = (float(weight_range[0]) + float(weight_range[1])) / 2
        weights.append(weight_avg)
    except:
        pass

    try:
        lifespan_range = cat['life_span'].split(' - ')
        lifespan_avg = (float(lifespan_range[0]) + float(lifespan_range[1])) / 2
        lifespans.append(lifespan_avg)
    except:
        pass

    # Country vs Breed
    origin = cat.get('origin', 'Unknown')
    name = cat.get('name', 'Unknown')
    countries.append(origin)
    breeds.append(name)

# Step 3: Stats calculate karo
def print_stats(title, data):
    print(f"\n📊 {title} Statistics:")
    print(f"Min: {min(data)}")
    print(f"Max: {max(data)}")
    print(f"Mean: {round(statistics.mean(data), 2)}")
    print(f"Median: {statistics.median(data)}")
    print(f"Standard Deviation: {round(statistics.stdev(data), 2)}")

print_stats("Weight (kg)", weights)
print_stats("Lifespan (years)", lifespans)

# Step 4: Frequency Table of Country vs Breed
df = pd.DataFrame({'Country': countries, 'Breed': breeds})
freq_table = df.groupby('Country')['Breed'].count().reset_index().sort_values(by='Breed', ascending=False)

print("\n🌍 Frequency Table: Country vs Number of Breeds")
print(freq_table)

'''3. Read the countries API and find
i. the 10 largest countries
ii. the 10 most spoken languages
iii. the total number of languages in the countries API'''
import requests
from collections import Counter

# Step 1: Fetch countries data
url = 'https://restcountries.com/v2/all'
response = requests.get(url)
countries = response.json()

# Step 2: Find 10 largest countries by area
largest_countries = sorted(
    [country for country in countries if 'area' in country and country['area'] is not None],
    key=lambda x: x['area'],
    reverse=True
)[:10]

print("🌐 Top 10 Largest Countries by Area:")
for country in largest_countries:
    print(f"{country['name']}: {country['area']} km²")

# Step 3: Count all spoken languages
language_counter = Counter()

for country in countries:
    for lang in country.get('languages', []):
        language_counter[lang['name']] += 1

# Step 4: Top 10 most spoken languages
most_spoken = language_counter.most_common(10)

print("\n🗣️ Top 10 Most Spoken Languages:")
for lang, count in most_spoken:
    print(f"{lang}: spoken in {count} countries")

# Step 5: Total number of unique languages
total_languages = len(language_counter)

print(f"\n📚 Total Number of Unique Languages: {total_languages}")

'''4. UCI is one of the most common places to get data sets for data science and
machine learning. Read the content of UCL
(https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will
be difficult, so you may try it with BeautifulSoup4'''
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

tables = soup.find_all('table', {'border': '1'})

dataset_names = []

for table in tables:
    links = table.find_all('a')
    for link in links:
        name = link.text.strip()
        if name:
            dataset_names.append(name)

print("Top 20 UCI Datasets:")
for i, name in enumerate(dataset_names[:20], start=1):
    print(f"{i}. {name}")
