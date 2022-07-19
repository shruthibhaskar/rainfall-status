import requests
import os
import json
from datetime import datetime

def env_check(env_var):
    if env_var in os.environ:
        return os.environ.get(env_var)
    else:
        raise ValueError('Set {0} Environment variable'.format(env_var))
        exit()
    
def fetch_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise ValueError('Please provide a valid Rainfall url, provided url is {0}'.format(url))
        exit()

def fetch_unit(data):
    unit = data['metadata']['reading_unit']
    return unit

def fetch_id(data, location):
    stations_dict = dict()
    stations = data['metadata']['stations'] 

    for station in stations:
        s_id = station['id']
        name = station['name']
        stations_dict[name] = s_id

    if location in stations_dict:
        return stations_dict[location]
    else:
        message = "Said location {0} cannot be found, Please provide a valid location".format(location)
        raise KeyError(message)
        exit()

def fetch_rainfall_status(data, id):
    items = data['items']
    readings_dict = dict()

    for item in items:
        readings = item["readings"]
        for reading in readings:
            value = reading["value"]
            s_id = reading["station_id"]
            readings_dict[s_id] = value

    reading_value = readings_dict[id]

    if (readings_dict[id] == 0):
        status = "Not Raining"
    else:
        status = "Raining"

    return status, reading_value