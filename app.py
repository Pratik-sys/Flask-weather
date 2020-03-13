from flask import Flask, url_for, render_template, request

import requests

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def weather():
    if request.method == "POST":
        city = request.form["city"]
    else:
        city = "nagpur"
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q="
        + city
        + "#"
        + "&units=metric"
    )


if __name__ == "__main__":
    app.run(debug=True)
