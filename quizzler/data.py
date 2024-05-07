import requests


parameters = {'amount' : 10,
              'difficulty' : 'easy',
              'type' : 'boolean'}
response = requests.get("https://opentdb.com/api.php", params=parameters)


data= response.json()

question_data = data['results']