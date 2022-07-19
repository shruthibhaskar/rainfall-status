import requests
import os
import json
from datetime import datetime

def fetch_api_data(url):

    response = requests.get(url)
    data = response.json()
    return data

def fetch_id(url, location):

    data = fetch_api_data(url)
    stations = data['metadata']['stations'] 

    for station in stations:
        id = station['id']
        name = station['name']
        stations_dict[name] = id

    return stations_dict[location]

def fetch_unit(url):

    data = fetch_api_data(url)
    unit = data['metadata']['reading_unit']
    return unit

def fetch_rainfall_status(url, id):

    data = fetch_api_data(url)
    items = data['items']
    readings_dict = dict()

    for item in items:
        readings = item["readings"]
        for reading in readings:
            value = reading["value"]
            s_id = reading["station_id"]
            readings_dict[s_id] = value

    reading_value=readings_dict[id]

    if (readings_dict[id] == 0):
        status="Not Raining"
    else:
        status="Raining"

    return status, reading_value

if __name__ == '__main__':

    api_url = "https://api.data.gov.sg/v1/environment/rainfall"
    location = "Upper Changi Road North"
    # location = "Tuas West Road"

    stations_dict = dict()
    unit = fetch_unit(api_url)
    # print(unit)
    id = fetch_id(api_url, location)
    # print(id)
    status = fetch_rainfall_status(api_url, id)
    # print(status)

    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M")
    # print("The current time is", currentTime)

    rainfall_amt = str(status[1])+unit
    print(location, currentTime, rainfall_amt, status[0])

    print_value = location+','+currentTime+','+rainfall_amt+','+status[0]
    print(print_value)
