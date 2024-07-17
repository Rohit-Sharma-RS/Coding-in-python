import os

import requests
import datetime

TODAY = datetime.date.today()
TODAY = (TODAY.strftime('%Y%m%d'))

OTHER_DAYS = datetime.date(day=12, year=2024, month=1).strftime('%Y%m%d')

USERNAME = os.environ.get('USERNAME')
pixela_api = "https://pixe.la/v1/users"

parameters = {
    "token": "hellohello",
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "thanksCode": "ThankYou"
}

graph_endpoint = f"{pixela_api}/{USERNAME}/graphs/graph1"

entry_parameters = {
    'date': TODAY,
    'quantity': '1',
}

post_parameters = {
    "id": "graph1",
    "name": "coding challenge",
    "unit": "days",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": os.environ.get('X_TOKEN')  # headers make the things more top secret so others can't find it
}

#making the graph
request = requests.post(graph_endpoint, json=post_parameters, headers=headers)

#adding pixels
pixel_post = requests.post(graph_endpoint, json=entry_parameters, headers=headers)

# output_api = f"https://pixe.la/@{USERNAME}"
# # print(pixel_post.json())
# output = requests.get(output_api)
# # print(output.text)
#
# login = requests.post(pixela_api, json=parameters)
# # print(request.text)


#deleting and updating
delete_api = f"{pixela_api}/{USERNAME}/graphs/graph1/{TODAY}"
# delete = requests.delete(delete_api, headers=headers)
# print(delete.text)

update_param = {
    "quantity": "3"
}

update = requests.put(delete_api, json=update_param, headers=headers)
print(update.text)
