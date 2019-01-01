#!/usr/bin/env python
# Learn how this works here: http://youtu.be/pxofwuWTs7c

import urllib
import urllib.request
import json
from math import trunc
api_key = 'c0a57aa83b4192bf30b977a0f83cb631'

#api.openweathermap.org/data/2.5/weather?zip={zip code},{country code}
#api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1111111111


# -------  SAMPLE OF WHAT API WILL RETURN ---------------
# {"coord":{"lon":-122.09,"lat":37.39},
# "sys":{"type":3,"id":168940,"message":0.0297,"country":"US","sunrise":1427723751,"sunset":1427768967},
# "weather":[{"id":800,"main":"Clear","description":"Sky is Clear","icon":"01n"}],
# "base":"stations",
# "main":{"temp":285.68,"humidity":74,"pressure":1016.8,"temp_min":284.82,"temp_max":286.48},
# "wind":{"speed":0.96,"deg":285.001},
# "clouds":{"all":0},
# "dt":1427700245,
# "id":0,
# "name":"Mountain View",
# "cod":200}


def weather_search(user_zip):
    api_call = 'http://api.openweathermap.org/data/2.5/weather?zip=' + str(user_zip) + '&APPID=' + api_key
    json_obj = urllib.request.urlopen(api_call)
    mydata = json.load(json_obj)



    print('The current temperature is: ' + str(kelvin_converter(mydata['main']['temp'])))
    print(mydata['name'])
    print('The sky conditions: ' + mydata['weather'][0]['main'])
    print(mydata['main'])
    print(mydata['sys'])
    print(mydata['wind'])

def kelvin_converter(kelvin):

    f = (kelvin - 273.15) * 9 / 5 + 32

    return trunc(f)


myzip = 47250
weather_search(myzip)