#! /usr/bin/python3

""" This program downloads weather data to a
    text file. """

import json
import requests
import sys

if len(sys.argv) < 2:
    print('Type in the City, comma, country (City, country).')
    sys.exit()

location = ''.join(sys.argv[1:])
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=9a39d5c0875169702eeceda684fc29c8' %(location)
page = requests.get(url)
page.raise_for_status()
weather = json.loads(page.text)


temp = weather['main']['temp']
temp = 9/5 * (temp - 273) + 32
temp = round(temp, 2)
description = weather['weather'][0]['description']


print('Current weather in %s:' %(location.split(',')[0]))
print(str(temp) + ' degrees, with ' + description + '.')
