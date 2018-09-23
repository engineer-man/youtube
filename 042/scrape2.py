import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('http://10.0.0.10:1234/scrape.html')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# get data simply by looking for each tr
data = []
for tr in soup.find_all('tr'):
	values = [td.text for td in tr.find_all('td')]
	data.append(values)

# get data only where rows are marked as special
data = []
for tr in soup.find_all('tr', { 'class': 'special' }):
	values = [td.text for td in tr.find_all('td')]
	data.append(values)

# get data within a specific element
data = []
div = soup.find('div', { 'class': 'special_table' })
for tr in div.find_all('tr'):
	values = [td.text for td in tr.find_all('td')]
	data.append(values)
