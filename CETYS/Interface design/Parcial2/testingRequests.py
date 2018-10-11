import requests

URL = 'http://graph.facebook.com/17841405822304914?fields=biography,id,username,website'
location = 'delhi technological university'

PARAMS = {'address':location}

r = requests.get(url = URL)

data = r.json()

##latitude = data['results'][0]['geometry']['location']['lat'] 
##longitude = data['results'][0]['geometry']['location']['lng'] 
##formatted_address = data['results'][0]['formatted_address'] 
  
# printing the output 
print(data)
