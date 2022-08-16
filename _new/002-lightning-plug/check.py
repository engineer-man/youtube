import requests
import json

# establish location
LAT = 30.3287
LNG = -87.1584

# get station and grid ids
url = f'https://api.weather.gov/points/{LAT},{LNG}'
station = requests.get(url)
station = station.json()
prop = station['properties']
grid_id = prop['gridId']
grid_x = prop['gridX']
grid_y = prop['gridY']

# get the forecast
url = f'https://api.weather.gov/gridpoints' \
      f'/{grid_id}/{grid_x},{grid_y}/forecast/hourly'
forecast = requests.get(url)
forecast = forecast.json()

today = forecast['properties']['periods'][0]
text = today['shortForecast']

# toggle power
url = f'http://10.0.0.174/cm'
if 'Thunderstorms Likely' in text:
    requests.get(f'{url}?cmnd=POWER+OFF')
else:
    requests.get(f'{url}?cmnd=POWER+ON')
