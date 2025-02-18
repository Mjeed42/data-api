# pylint: disable=missing-module-docstring
"""
This module provides functionality to search for a city and retrieve its
weather forecast.
"""
import sys
import requests

BASE_URI = "https://weather.lewagon.com"

def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user
    choose between them.
    Return one city (or None).
    '''
    url = f"{BASE_URI}/geo/1.0/direct?q={query}&limit=5"
    response = requests.get(url).json()

    if not response:
        print("City not found. Please try again.")
        return None

    if len(response) == 1:
        return response[0]

    print("Multiple matches found:")
    for i, city in enumerate(response, start=1):
        print(f"{i}. {city['name']}, {city.get('country', 'N/A')}")

    choice = int(input("Which city did you mean?\n> ")) - 1
    return response[choice]

def weather_forecast(lat, lon):
    '''
    Return a 5-day weather forecast for the city,
    given its latitude and longitude.
    '''
    forecast_url = f"{BASE_URI}/data/2.5/forecast?lat={lat}&lon={lon}&limit=5"
    forecast_response = requests.get(forecast_url).json()
    forecasts = []

    for forecast in forecast_response['list']:
        date = forecast['dt_txt'].split()[0]
        weather = forecast['weather'][0]['description']
        temp = forecast['main']['temp_max']

        if not forecasts or forecasts[-1]['date'] != date:
            forecasts.append({
                'date': date,
                'weather': weather,
                'temp': temp
            })

    return forecasts

def main():
    '''Ask user for a city and display weather forecast'''
    query = input("City?\n> ")
    city = search_city(query)

    if city:
        lat, lon = city['lat'], city['lon']
        forecasts = weather_forecast(lat, lon)
        for forecast in forecasts:
            print(f"""Date: {forecast['date']}, Weather: {forecast['weather']},
                  Max Temp: {forecast['temp']}°C""")
    else:
        print("No city selected.")

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
