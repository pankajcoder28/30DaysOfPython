#1. Read the hacker_news.csv file from data directory
import pandas as pd
d = pd.read_csv('hacker_news.csv')
#2. Get the first five rows
print(d.head())
#3. Get the last five rows
print(d.tail())
#4. Get the title column as pandas series
print(d['title'])
#5. Count the number of rows and columns
print(d.shape)
#o Filter the titles which contain python
python_title = d[d['title'].str.contains('python',case=False)]
print(python_title)
javascript_title = d[d['title'].str.contains('javascript',case=False)]
print(javascript_title)
