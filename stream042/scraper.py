import requests
import json
from bs4 import BeautifulSoup

html = requests.get('https://www.yardsalesearch.com/garage-sales.html?zip=90210').text

soup = BeautifulSoup(html, 'html.parser')

table = []

for element in soup.find_all('div', { 'class': 'event row featured'}):
    row = []

    row.append(element.find('span', { 'itemprop': 'streetAddress' }).text)
    row.append(element.find('span', { 'itemprop': 'addressLocality' }).text)
    row.append(element.find_all('span', { 'itemprop': 'addressRegion'})[0].text)
    row.append(element.find_all('span', { 'itemprop': 'addressRegion'})[1].text)
    row.append(element.find('meta', { 'itemprop': 'latitude' })['content'])
    row.append(element.find('meta', { 'itemprop': 'longitude' })['content'])
    row.append(element.find('meta', { 'itemprop': 'startDate' })['content'])
    row.append(element.find('meta', { 'itemprop': 'endDate' })['content'])

    table.append(row)

print('address,city,state,zip,lat,lng,start,end')
for row in table:
    print(','.join(row))
