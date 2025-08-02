import requests
import json
import gzip
import random
API_KEY = '***REMOVED***'
URl = 'http://api.openweathermap.org/data/2.5/weather?'

with gzip.open("city.list.json.gz", "rt", encoding="utf-8") as cities:
    all_cities = json.load(cities)

    random_cities = random.sample(all_cities, 5)

    for city in random_cities:
        print(city)

