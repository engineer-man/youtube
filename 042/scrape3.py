import requests
from bs4 import BeautifulSoup

# get the data
data = requests.get('https://umggaming.com/leaderboards')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

leaderboard = soup.find('table', { 'id': 'leaderboard-table' })
tbody = leaderboard.find('tbody')

for tr in tbody.find_all('tr'):
	place = tr.find_all('td')[0].text.strip()
	username = tr.find_all('td')[1].find_all('a')[1].text.strip()
	xp = tr.find_all('td')[3].text.strip()
	print(place, username, xp)
