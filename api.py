import requests
token =  SECRET

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
