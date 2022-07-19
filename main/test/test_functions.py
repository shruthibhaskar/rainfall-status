import requests, os, json
from datetime import datetime
import sys
sys.path.insert(0, '/Users/shruthibhaskar/Work/Shruthi_Bhaskar/Dell/code/main/app')
from functions import fetch_unit, fetch_id, fetch_rainfall_status, env_check

def fetch_api_data(test_json_file):
    f = open(test_json_file)
    data = json.load(f)
    f.close()
    return data

def test_raining(test_json_file, location):
    print('To test Raining status for {0} location'.format(location))
    data = fetch_api_data(test_json_file)
    unit = fetch_unit(data)
    station_id = fetch_id(data, location)
    status = fetch_rainfall_status(data, station_id)
    current_time = "12:10"
    rainfall_amt = str(status[1])+unit
    raining_status = status[0]
    print_value = location+', '+current_time+', '+rainfall_amt+', '+raining_status
    print(print_value, '\n')
    return print_value

def test_not_raining(test_json_file, location):
    print('To test Raining status for {0} location'.format(location))
    data = fetch_api_data(test_json_file)
    unit = fetch_unit(data)
    station_id = fetch_id(data, location)
    status = fetch_rainfall_status(data, station_id)
    current_time = "12:10"
    rainfall_amt = str(status[1])+unit
    raining_status = status[0]
    print_value = location+', '+current_time+', '+rainfall_amt+', '+raining_status
    print(print_value, '\n')
    return print_value

def test_location(test_json_file, location):
    print('Fetch station_id of {0} location'.format(location))
    data = fetch_api_data(test_json_file)
    station_id = fetch_id(data, location)
    print('Station id of {0} location is {1}'.format(location,station_id),'\n')
    return station_id

def test_env_check():
    print('Check environment variable LOCATION value')
    location = env_check("LOCATION")
    print('LOCATION = {0}'.format(location),'\n')
    return location
