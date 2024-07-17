import os
import requests
from datetime import *
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_API_KEY = os.environ.get('STOCK_KEY')
api = 'https://www.alphavantage.co/query'
STOCK_PARAM = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "output_size": "full",
    "apikey": STOCK_API_KEY
}

yesterday = str(date.today() - timedelta(days=1))
day_before = str(date.today() - timedelta(days=2))

stock_request = requests.get(api, params=STOCK_PARAM)
data = stock_request.json()

# stock_yesterday_open = float(data["Time Series (Daily)"][yesterday]['1. open'])
stock_yesterday_close = float(data["Time Series (Daily)"][yesterday]['4. close'])
# stock_daybefore_open = float(data["Time Series (Daily)"][day_before]['1. open'])
stock_daybefore_close = float(data["Time Series (Daily)"][day_before]['4. close'])

percent_change = (stock_yesterday_close - stock_daybefore_close) * 100 / stock_daybefore_close

if percent_change > 0.1:
    string = f"TSLA:🔺{round(percent_change, 2)}"
elif percent_change < -0.1:
    string = f"TSLA:🔻{round(percent_change, 2)}"
else:
    print("not")
    print(percent_change)


para = ""
NEWS_API_KEY = os.environ.get('NEWS_API')
news_api = 'https://newsapi.org/v2/everything'
news_param = {'q': "RELIANCE",
              'from': day_before,
              'sortBy': 'popularity',
              'apiKey': NEWS_API_KEY
}

news_request = requests.get(news_api,params=news_param)
data = news_request.json()
ls=[]
for i in range(3):
    title = data['articles'][i]['title']
    description = data['articles'][i]['description']
    ls.append(f"{title}\n{description}\n")

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')
client = Client(account_sid, auth_token)
message = client.messages.create(body=f"{string}\n{str(ls)}",
                                from_=os.environ.get('P1'),
                                to=os.environ.get('P2'))


