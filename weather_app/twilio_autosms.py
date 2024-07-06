import os

from twilio.rest import Client


class Msg:
  def __init__(self):
    self.account_sid = os.environ.get('ACCOUNT_SID')
    self.auth_token = os.environ.get('AUTH_TOKEN')
    self.client = Client(self.account_sid, self.auth_token)

    self.message = self.client.messages.create(body="It is going to rain. Remember to bring an ☂Umbrella :)",
                                   from_= os.environ.get('PHONE'),
                                   to= os.environ.get('MY_PHONE'))