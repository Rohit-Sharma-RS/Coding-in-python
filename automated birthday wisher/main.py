import datetime as dt
import os

import pandas as pd
import smtplib
import random

# 1. Update the birthdays.csv
dictionar = {'name': ['brother', 'Abhay', 'Keshav'],
             'email': ['input the email of your loved ones'],
             'year': ['2007', '1973', '1975'], 'month': [12, 12, 12], 'date': [25, 10, 11]}
dictionary = pd.DataFrame.from_dict(dictionar)
dictionary.to_csv("Birthday.csv")
file = pd.read_csv("Birthday.csv")


# 2. Check if today matches a birthday in the birthdays.csv
today = dt.datetime.today()
for index, rows in file.iterrows():
    if today.day == rows['date'] and today.month == rows['month']:
        birthday_msg = str(random.choice(os.listdir('letter_templates')))
        email_sending_to = rows['email']
        with open(f'letter_templates/{birthday_msg}', 'r+') as f:
            data = f.read()
            data = data.replace('[NAME],',f'{rows["name"]},')


username = "your email"
password = "yourpassword"

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user = username, password=password)
connection.sendmail(from_addr=username,
                    to_addrs=email_sending_to,
                    msg=f"Subject:Happy birthday \n\n {data}")
connection.close()

