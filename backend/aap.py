import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import pymongo

load_dotenv()

MONGO_URL = os.getenv("MONGO_URI")

client = pymongo.MongoClient(
    MONGO_URL,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000
)

db = client.test
collection = db["new_project"]

app = Flask(__name__)


@app.route("/submit", methods=["POST"])
def submit():

    formdata = request.get_json()

    if not formdata:
        return {"error": "No data received"}, 400

    collection.insert_one(formdata)

    return {"message": "Data saved successfully"}, 200


@app.route("/view")
def view():

    data = list(collection.find({}, {"_id": 0}))

    return jsonify({"data": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)