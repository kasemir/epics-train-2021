# Python program to find current weather details of any city
# using openweathermap api
 
# import required modules
import requests, json
from pprint import pprint
 
# Enter your API key here
default_api_key = 'daf4cf281052dc65e4728f7de616032c'
 
# base_url variable to store url
base_url = 'http://api.openweathermap.org/data/2.5/weather?'

def getWeather(city='Paris', units='imperial', api_key=default_api_key, debug=False):
    url = f'{base_url}appid={api_key}&q={city}&units={units}'
    if debug:
        print(f'Fetching data from {url}')
    response = requests.get(url).json()
    if int(response['cod']) == 404:
        raise UserWarning(f'City {city} not found')
    if int(response['cod']) != 200:
        raise UserWarning(f'Received invalid response {response["cod"]}')
    
    #pprint(response)

    weather = {
        'temperature': response['main']['temp'],
        'humidity':    response['main']['humidity'],
        'pressure':    response['main']['pressure'],
        'clouds':      response['weather'][0]['description'],
        'wind':        response['wind']['speed'],
        'icon':        response['weather'][0]['icon'],
    }

    return weather

if __name__ == '__main__':
    weather = getWeather(city='Barcelona',debug=True)
    pprint(weather)
