#ce481094d9296526df5a1ecf225cc7fc0237d0da9aa61c8ae23cab4eacfc73f4

import requests
token =  "ce481094d9296526df5a1ecf225cc7fc0237d0da9aa61c8ae23cab4eacfc73f4"

headers = {
    "Authorization": "Bearer %s" % token,
}

def get():
    response = requests.get('https://api.lifx.com/v1/lights/all', headers = headers)
    print (str(response))
    input()
    return response

def put(payload):
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
