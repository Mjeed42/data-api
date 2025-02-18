# pylint: disable=missing-docstring,invalid-name

"""
This module tests the functionality of the Le Wagon Weather API by fetching city data.
"""

import requests

def fetch_city_data(city_name):
    """
    Fetches city data from the Le Wagon Weather API.

    Args:
        city_name (str): The name of the city to fetch data for.

    Returns:
        dict: A dictionary containing city data (name, latitude, longitude).
    """
    url = f"https://weather.lewagon.com/geo/1.0/direct?q={city_name}"
    response = requests.get(url).json()
    return response[0]

def main():
    """
    Main function to fetch and display city data.
    """
    city_name = "Barcelona"
    city = fetch_city_data(city_name)
    print(f"{city['name']}: ({city['lat']}, {city['lon']})")
