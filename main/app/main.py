from flask import Flask
from datetime import datetime
import os, logging, sys
from functions import fetch_id,fetch_unit,fetch_rainfall_status,env_check,fetch_api_data

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.disabled = False    

@app.route('/')

def rainfall_data():
    api_url = env_check("API_URL")
    location = env_check("LOCATION")
    print('\n',"Env values are API_URL:{0}, LOCATION:{1}".format(api_url,location))

    data = fetch_api_data(api_url)
    unit = fetch_unit(data)
    station_id = fetch_id(data, location)
    status = fetch_rainfall_status(data, station_id)

    current_date_time = datetime.now()
    current_time = current_date_time.strftime("%H:%M")

    rainfall_amt = str(status[1])+unit
    raining_status = status[0]
    print('\n',"Fetching rainfall status for {0} location".format(location))
    print_value = location+', '+current_time+', '+rainfall_amt+', '+raining_status
    print(print_value,'\n')

    return print_value

if __name__ == '__main__':
    print('\n','Rainfall Service Running...','\n')
    app.run(host='0.0.0.0',port=8080)
