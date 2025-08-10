***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
from dotenv import load_dotenv
import os

load_dotenv()

KEY = os.getenv('API_KEY')
URL = 'http://api.openweathermap.org/data/2.5/weather?'


def get_cities():
    with gzip.open("city.list.json.gz", "rt", encoding="utf-8") as cities:
        all_cities = json.load(cities)
        return all_cities


def get_five_cities():
    current_five_cities = {}
    cities = get_cities()
    random_cities = random.sample(cities, 5)

***REMOVED***
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