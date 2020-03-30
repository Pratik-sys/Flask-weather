import requests
from flask import Flask, url_for, render_template, request
from dotenv import load_dotenv
import os, json

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def weather():
    if request.method == "POST":
        city = request.form["city"]
    else:
        city = "nagpur"
    api_key = os.getenv("PROJECT_API_KEY")
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?"
        + "appid="
        + api_key
        + "&q="
        + city
        + "&units=metric"
    )

    retrieve = response.json()
    with open("city.json", "w") as json_file:
        json.dump(retrieve, json_file)
    data = {
        "city": retrieve["name"],
        "temprature": str(retrieve["main"]["temp"]),
        "humidity": str(retrieve["main"]["humidity"]),
        "pressure": str(retrieve["main"]["pressure"]),
        "description": str(retrieve["weather"][0]["description"]),
        "icon": retrieve["weather"][0]["icon"],
    }
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
