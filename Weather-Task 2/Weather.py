import statistics
from tkinter import messagebox
import requests
import json
import gzip
import random
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv('API_KEY')
URL = 'http://api.openweathermap.org/data/2.5/weather?'

current_five_cities = {}
def get_cities():
    with gzip.open("city.list.json.gz", "rt", encoding="utf-8") as cities:
        all_cities = json.load(cities)
        return all_cities


def get_five_cities():
    global current_five_cities
    current_five_cities = {}
    cities = get_cities()
    random_cities = random.sample(cities, 5)

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

            current_five_cities[city_name] = {
                "temp": data["main"]["temp"],
                "desc": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"]
            }

        except requests.RequestException as e:
            print(e)

    return current_five_cities


def search_city(city_name):
    isFound = False
    searched_city= get_cities()
    for city in searched_city:
        if city['name'].lower() == city_name.lower():
            city_id = city['id']
            name = city['name']
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

            return  {
                    "name": name,
                    "desc": data["weather"][0]["description"],
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"]
            }
        except requests.RequestException as e:
            print(e)
    else:
        messagebox.showinfo(f"City {city_name} not found", "City not found")
    return None

def get_stats():
    sorted_cities = dict(sorted(current_five_cities.items(), key=lambda x: x[1]["temp"]))
    coldest_city, data = next(iter(sorted_cities.items()))
    coldest_temp = data["temp"]
    avg_temp = statistics.mean(d["temp"] for d in sorted_cities.values())
    return coldest_city, coldest_temp, avg_temp