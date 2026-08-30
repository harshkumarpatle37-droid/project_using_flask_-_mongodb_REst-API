import os
from dotenv import load_dotenv
from flask import Flask, render_template,request
import requests
load_dotenv()

BACKEND_URL ='http://127.0.0.1:9000'

app = Flask(__name__)  # Renamed to app for consistency


@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/submit', methods=['POST'])  
def submit():
    form_data = dict(request.form) 

    requests.post(BACKEND_URL +'/submit', json=form_data)

    

    return ('data received successful')

@app.route('/view_data')
def view_data():
    response = requests.get(BACKEND_URL +'/view')

    data= response.json()

    data ['hello']= 'world'

    return data
  



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)