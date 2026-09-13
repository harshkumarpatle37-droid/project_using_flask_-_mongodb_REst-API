import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
import requests

load_dotenv()

# Render backend URL
BACKEND_URL = "https://project-using-flask-mongodb-rest-api-1.onrender.com"

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    # Get form data from frontend
    formdata = dict(request.form)

    # Send data to Render backend
    response = requests.post(
        BACKEND_URL + "/submit",
        json=formdata
    )

    if response.status_code == 200:
        return "Data received successfully"

    return "Error while saving data", 500


@app.route("/view_data")
def view_data():

    # Get data from Render backend
    response = requests.get(BACKEND_URL + "/view")

    if response.status_code == 200:
        data = response.json()
        return data

    return {"error": "Could not fetch data"}, 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )