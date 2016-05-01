#c1229c312e86cc5f733a7d9b41fba6728d92fe4469514e8f4d34db7b67bc0362

import requests
token =  "c1229c312e86cc5f733a7d9b41fba6728d92fe4469514e8f4d34db7b67bc0362"

headers = {
    "Authorization": "Bearer %s" % token,
}

def get():
    response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)
    print (str(response))
    input()
    return response

def put(payload):
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
