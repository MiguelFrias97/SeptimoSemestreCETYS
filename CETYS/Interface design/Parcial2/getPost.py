import requests
import time
import json
import datetime

def example(i):
    url = "http://10.12.10.191/API/Sensors"


    headers = {'Content-Type': "application/json"}
    data = {"id":str(i),"date":"1/1/2018 18:00:03","strain": [1,2,3,1,244,1,25,9],"displacement": [3,1,2,3,24,124,1,5]}
    data2send = json.dumps(data)
    response = requests.request("POST", url, data=data2send, headers=headers)

    print(response)

i=0
while True:
    r = requests.get(url='http://10.12.10.191/API/Test')
    d = int(r.text[1:2])
    if d == 1:
        example(i)
    elif d == 0:
        print("No enviado")
    input('')
    i += 1
