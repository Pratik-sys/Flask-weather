from flask import Flask, url_for, render_template, request
from dotenv import load_dotenv
import os
import requests

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
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city
        + api_key
        + "&units=metric"
    )


if __name__ == "__main__":
    app.run(debug=True)
