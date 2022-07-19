from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def func():
    print (os.environ.get('API_URL'))
    print (os.environ.get('LOCATION'))
    val = os.environ.get('API_URL') + " " + os.environ.get('LOCATION')
    return val

app.run(host='0.0.0.0',port=8080)
