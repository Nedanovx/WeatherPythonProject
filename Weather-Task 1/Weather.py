import load_dotenv
import requests
import json
import gzip
import random
import statistics
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv('API_KEY')
URL = 'http://api.openweathermap.org/data/2.5/weather?'

current_five_cities = {}
with gzip.open("city.list.json.gz", "rt", encoding="utf-8") as cities:
    all_cities = json.load(cities)

    random_cities = random.sample(all_cities, 5)

    for city in random_cities:
        city_id = city['id']
        city_name = city['name']

        params = {
            'id': city_id,
            'appid': KEY,
            'units': 'metric',
            'lang': 'en'
        }
        try:
            response = requests.get(URL, params=params)
            response.raise_for_status()
            data = response.json()

            description = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']

            current_five_cities[city_name] = temp
            sorted_cities = dict(sorted(current_five_cities.items(), key=lambda x: x[1]))
            print(f"city: {city_name}")
            print(f"The weather is: {description}")
            print(f"The temperature is: {temp}°C") # alt+0176
            print(f"Humidity is: {humidity}%")
            print()
        except requests.RequestException as e:
            print(e)
    city, temp = next(iter(sorted_cities.items()))
    print(f"Coldest city: {city}")
    print(f"Temperature: {temp}°C")
    print(f"Average temperatures: {statistics.mean(sorted_cities.values()):.2f}°C")

user_input = input("Which city would you like to see? ").strip().lower()

isFound = False

for city in  all_cities:
    if city['name'].lower() == user_input:
        city_id = city['id']
        city_name = city['name']
        isFound = True
        break
if isFound:
    params = {
        'id': city_id,
        'appid': KEY,
        'units': 'metric',
        'lang': 'en'
    }
    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()

        description = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']

        print(f"city: {city_name}")
        print(f"The weather is: {description}")
        print(f"The temperature is: {temp}°C")
        print(f"Humidity is: {humidity}%")
    except requests.RequestException as e:
        print(e)
else:
    print(f'city: {user_input} not found')