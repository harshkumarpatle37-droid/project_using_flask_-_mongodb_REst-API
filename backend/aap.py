import os
from dotenv import load_dotenv
from flask import Flask,request,jsonify
import pymongo

load_dotenv()

MONGO_URL = os.getenv('MONGO_URI')
# Fixed: Pass the variable MONGO_URL instead of string "MONGO_URI"
client = pymongo.MongoClient(MONGO_URL)

db = client.test
collection = db['new_project']

app = Flask(__name__)  # Renamed to app for consistency

@app.route('/submit', methods=['POST'])
def submit():

    formdata = request.get_json()

    if not formdata:
        return {"error": "No data received"}, 400

    collection.insert_one(formdata)

    return {"message": "Data saved successfully"}, 200
    
## THIS IS ONLLY  for A TEST 
@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)

        del item['_id']

    data = {
            'data': data
        }

    print(data)

    return jsonify(data)



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)