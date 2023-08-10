#!/usr/bin/env python3

# import library
from urllib.request import urlopen
import json
from ics import Calendar, Event

def main():
    fetchEvents()

def fetchEvents():
    # store the URL in url as 
    # parameter for urlopen
    url = "https://raw.githubusercontent.com/bigfoott/ScrapedDuck/data/events.json"
    
    # store the response of URL
    response = urlopen(url)
    
    # storing the JSON response 
    # from url in data
    data_json = json.loads(response.read())
    
    communityDays = [x for x in data_json if x['eventType'] == 'community-day']
    # print the json response
    # print(json.dumps(communityDays, indent=2))

    createCal(communityDays)

def createCal(communityDays):
    calender = Calendar()

    # create events from json data
    for event in communityDays:
        e = Event()
        e.name = event["name"]
        e.begin = event["start"]
        e.end = event["end"]
        calender.events.add(e)
    
    # print(calender.events)
    with open('community_day.ics','x') as my_file:
        my_file.writelines(calender.serialize_iter())


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()