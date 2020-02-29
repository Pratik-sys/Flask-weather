import requests, json 
import os
from dotenv import load_dotenv
load_dotenv()

def weather(city):
    api_key = os.getenv("PROJECT_API_KEY")

    api_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = api_url + "appid=" + api_key + "&q=" + city

    response = requests.get(complete_url)

    retrieve = response.json()
    with open('city.json', 'w') as json_file:
        json.dump(retrieve, json_file)

weather(input("Enter the city name:"))
