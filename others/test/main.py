from flask import Flask
from datetime import datetime
import requests
import os
import json
from test_functions import fetch_api_data,fetch_id,fetch_unit,fetch_rainfall_status,test_raining,fetch_api_data_url

app = Flask(__name__)

@app.route('/')

def rainfall_data():
    api_url = os.environ.get('API_URL')
    print(api_url)
    fetch_api_data_url(api_url)
    return api_url

app.run(host='0.0.0.0',port=8080)
