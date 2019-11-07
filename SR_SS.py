import requests
from geopy.geocoders import Nominatim
# from geopy.geocoders.options.default_user_agent = "my-application"
location = Nominatim(user_agent="my-application").geocode('Moscow')
r = requests.get('https://api.sunrise-sunset.org/json', params={'lat': location.latitude, 'lng': location.longitude}).json()['results']
print('Sunrise:', r['sunrise'])
print('Sunset:', r['sunset'])
