#1. Scrape the following website and store the data as json file
import requests
from bs4 import BeautifulSoup
url = 'http://www.bu.edu/president/boston-university-facts-stats/'
responce = requests.get(url)
status = responce.status_code
print(status)
content = responce.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title.get_text())
print(soup.body.get_text())
print(responce.status_code)

facts_section = soup.find('div', class_='facts-stats')
facts_list = facts_section.find_all('li') if facts_section else []

data = [li.get_text(strip=True) for li in facts_list]
import json
with open('file.json','w')as f:
    json.dump(data,f,indent=4)

'''2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and
change it to a json file'''

url = 'https://archive.ics.uci.edu/ml/datasets.php'
res = requests.get(url)
con = res.content
soup = BeautifulSoup(con , "html.parser")
print(soup.title.get_text())
print(soup.body.get_text())
print(res.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0]
for td in table.find('tr').find_all('td'):
    print(td.text)

dataset_list = []

for row in table.find_all('tr')[1:]:  # Skip header row
    cols = row.find_all('td')
    if len(cols) >= 5:
        dataset = {
            'Name': cols[0].get_text(strip=True),
            'Data Types': cols[1].get_text(strip=True),
            'Default Task': cols[2].get_text(strip=True),
            'Attribute Types': cols[3].get_text(strip=True),
            'Instances': cols[4].get_text(strip=True),
        }
        dataset_list.append(dataset)

with open('uci_datasets.json', 'w') as f:
    json.dump(dataset_list, f, indent=4)

print("Data saved to uci_datasets.json")

'''3. Scrape the presidents table and store the data as
json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States).
The table is not very structured and the scrapping may take very long time.'''

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='wikitable')
rows = table.find_all('tr')[1:]  # Skip header row

presidents = []

for row in rows:
    cols = row.find_all(['th', 'td'])
    if len(cols) >= 5:
        name = cols[1].get_text(strip=True)
        term = cols[2].get_text(strip=True)
        party = cols[3].get_text(strip=True)
        vice_president = cols[4].get_text(strip=True)

        presidents.append({
            "Name": name,
            "Term": term,
            "Party": party,
            "Vice President": vice_president
        })
with open("us_presidents.json", "w", encoding="utf-8") as f:
    json.dump(presidents, f, indent=4, ensure_ascii=False)
