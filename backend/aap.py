import os
from dotenv import load_dotenv
from flask import Flask,request
import pymongo

load_dotenv()

MONGO_URL = os.getenv('MONGO_URI')
# Fixed: Pass the variable MONGO_URL instead of string "MONGO_URI"
client = pymongo.MongoClient(MONGO_URL)

db = client.test
collection = db['new_project']

app = Flask(__name__)  # Renamed to app for consistency

@app.route('/submit', methods=['POST'])  # Fixed: methods (plural) and POST
def submit():

    formdata = dict(request.json) 

    collection.insert_one (formdata)

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    collection.insert_one({'name': name, 'email': email, 'phone': phone})

    return ('success.html')
    
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

    return data 



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)