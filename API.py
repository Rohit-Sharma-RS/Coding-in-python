import requests

response = requests.get(url = 'http://api.open-notify.org/iss-now.json')
if(response.status_code != 200):
    raise Exception("Error communicating")
else:
    data = response.json()
    longitude = data['iss_position']['longitude']
    latitude = data['iss_position']['latitude']
    issposition = (latitude,longitude)
    print(issposition)
