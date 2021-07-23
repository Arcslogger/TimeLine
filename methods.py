import populartimes
import requests
from datetime import datetime
from operator import itemgetter
import json

def init (): # read all sensitive information (google API keys, data files, etc) from a sepearate file
    with open('keys.json', 'r') as f:
        return json.load(f)

def query (types, address, radius): # makes api calls to retrive PopularTimes data 
    # prep for api calls
    keys = init()
    base_url = keys['base_url']
    key = keys['key']
    url = base_url+"address="+address+"&key="+key
    path = keys['path']
    # call Geocoding api to convert addresses into geo-coordiantes
    response = requests.request("GET", url) 
    with open(path, 'w') as f:
        json.dump(response.json(), f, indent=4)
    with open(path, 'r') as f:
        data = json.load(f)
    lat = data["results"][0]["geometry"]["location"]['lat']
    lng = data["results"][0]["geometry"]["location"]['lng']
    rad = float(radius) / 111000.0
    #calculate the area range that the user wants to search
    lower = [lat - rad, lng - rad]
    upper = [lat + rad, lng + rad]
    #call the PopularTimes API and return the results
    return populartimes.get(key, [types], (lower[0], lower[1]), (upper[0], upper[1]))

def writeFile (list): # takes PopularTimes data and formats a JSON file to be passed to the front end
    path = init()['path'] # JSON path 
    currTime = int(datetime.now().strftime("%H"))
    currDate = datetime.today().weekday()
    locations = [] #list of all locations found by API call
    for entry in list: #retrieves appropriate information from API calls and appends them to the JSON file 
        name = entry['name']
        busyness = entry['populartimes'][currDate]['data'][currTime - 1]
        address = entry['address']
        try:
            rating = entry['rating'] #attempts to get a rating for the location if one is available
        except KeyError:
            rating = None
        if busyness > 0:
            locations.append({'name':name,'busyness':busyness,'rating':rating,'address':address})
    #sorts the list from least to most busy by default
    locations = sorted(locations, key=itemgetter('busyness'), reverse=False)
    #writes to JSON file
    with open (path, 'w') as f:
        json.dump(locations, f, indent=4)
    
#EXAMPLE CALL:
#writeFile(query('restaurant','1 Dundas St E', '100'))
