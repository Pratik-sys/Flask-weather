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
    with open("city.json", "w") as json_file:
        json.dump(retrieve, json_file)

    # this will check the stauts if it is "404" or not.
    if retrieve["cod"] != "404":
        collect = retrieve["main"]

        # store the corresponding value
        # All the vlaues that will reflect in termianl are in "kelvin"

        current_temprature = collect["temp"]

        current_Humidity = collect["humidity"]

        current_pressure = collect["pressure"]

        # We need the weather description
        # we make the store the data in another variable.

        data = retrieve["weather"]
        # we will stor the key at zeroth index of data
        weather_description = data[0]["description"]

        print(
            f"Temprature(in Kelvin) = {current_temprature} \n Humidity(in %) = {current_Humidity} \n Atmosphric_pressure = {current_pressure} \n Description = {weather_description}"
        )

    else:
        print("City not found please refer Map")


weather(input("Enter the city name:"))
