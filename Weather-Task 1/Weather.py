***REMOVED***
***REMOVED***
***REMOVED***
***REMOVED***
API_KEY = '***REMOVED***'
URL = 'http://api.openweathermap.org/data/2.5/weather?'

current_five_cities = {}
with gzip.open("city.list.json.gz", "rt", encoding="utf-8") as cities:
    all_cities = json.load(cities)

***REMOVED***

***REMOVED***
        city_id = city['id']
        city_name = city['name']

        params = {
            'id': city_id,
            'appid': API_KEY,
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

