import requests
import os
import json

import json

def main():

    api_url = "https://api.data.gov.sg/v1/environment/rainfall"

    response = requests.get(api_url)

    data = response.json()
    print(type(data))
    print(type(data['metadata']))
    print(data['metadata'])
    print('\n')

    print(type(data['metadata']['stations']))
    print((data['metadata']['stations']))
    print('\n')

    print(type(data['items']))
    print(data['items'])
    print('\n')
    stations = data['metadata']['stations']
    print(type(stations))
    # for station in stations:
    #     print(station['id'], station['name'])
    #     print(station['location']['latitude'],station['location']['longitude'])
# create new dict
# stations_dict = dict()

    for station in data['metadata']['stations']:
        print(station['id'], station['name'])
        print(station['location']['latitude'],station['location']['longitude'])
        id = station['id']
        name = station['name']
        stations_dict[name] = id

if __name__ == '__main__':
    stations_dict = dict()
    main()
    print('\n')
    print(stations_dict["Towner Road"])
