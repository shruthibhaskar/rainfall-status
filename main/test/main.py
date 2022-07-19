from flask import Flask
from datetime import datetime
import requests
import os, logging
import json
from test_functions import fetch_api_data,fetch_id,fetch_unit,fetch_rainfall_status,test_raining

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = True    

@app.route('/')

def rainfall_data():
    api_url = os.environ.get('API_URL')
    print(api_url)
    return api_url

if __name__ == '__main__':
    print('\n','Rainfall Service Running...','\n')
    app.run(host='0.0.0.0',port=8080)
