import requests
import json
import os

ABSOLUTE_ZERO = -273.15

def get_data(city, country="ca"):
    with open('keys/OpenWeatherKey.txt','r') as api_key:
        api_key = api_key.read().rstrip()
    raw_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city},{country}&APPID={api_key}').text
    response = json.loads(raw_response)
    dir_check("json")
    with open(f'json/OpenWeather-{city}-{country}.json','w') as file:
       json.dump(response, file)

def dir_check(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def format_weather(city, country="ca"):
    get_data(city, country)
    with open(f'json/OpenWeather-{city}-{country}.json','r') as file:
        response = json.load(file)

    out = city.upper() + " (" + country.upper() + ")" + "\n"

    try:
        out += "    Error : " + response['message']
        os.remove(f'json/OpenWeather-{city}-{country}.json') 
        return out
    except:
        pass
    
    out += "    Location       : " + str(response['coord']['lon']) + "°N " + str(response['coord']['lat']) + "°W" + "\n"
    out += "    Condition      : " + response['weather'][0]['main'] + "\n"
    out += "    Temperature    : " + format(response['main']['temp'] + ABSOLUTE_ZERO,'.2f') + "°C" + "\n"
    out += "    Apparent temp  : " + format(response['main']['feels_like'] + ABSOLUTE_ZERO,'.2f') + "°C" + "\n"
    out += "    Min temp       : " + format(response['main']['temp_min'] + ABSOLUTE_ZERO,'.2f') + "°C" + "\n"
    out += "    Max temp       : " + format(response['main']['temp_max'] + ABSOLUTE_ZERO,'.2f') + "°C" + "\n"
    return out