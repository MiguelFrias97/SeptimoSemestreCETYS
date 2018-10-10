import requests

wurl = 'http://maps.googleapis.com/maps/api/geocode/json'

location = 'delhi technological university'

PARAMS= {'address':location}

r = requests.get(url = wurl, params = PARAMS)

data = r.json()
