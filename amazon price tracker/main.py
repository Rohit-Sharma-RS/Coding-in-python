import os

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

email = "vampire.instinct777@gmail.com"
password = os.getenv('PASSWORD')

header = {'Accept_Language':'en-US,en;q=0.6',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

expected = 900.0

response = requests.get('https://www.amazon.in/Atomic-Habits-Courage-Disliked-happiness/dp/B09GY8ZYL5/ref=sr_1_10?crid=97FAT064I137&dib=eyJ2IjoiMSJ9.iE8Wl3oAt9X0ax5skHc6Nx_YxuwStQFl17qO2fj0BaivsY-WWKAYRHb2cBoAMtffc7sHFnKDT0_Nk084f-k7gY55r2uvr1OiyHp7FGVPBvNWtmCQvW2Z93AgigL2h-keElpSj48dXl05O3z_l1GmNTMRXhB2rMkTd7E-GSird5nVrzYmQN-xEOgT3uFuGWZq_sdFvJxFZSHh719DKAtpid_2VIxrV6luanVh-ZNQyHw.5njo6lcDAw6JtMnnvBlQUD-ngXVg9vc8wUSncnLEStA&dib_tag=se&keywords=atomic+habits+book+english&qid=1709485297&sprefix=atomic+habits+book+englisj%2Caps%2C213&sr=8-10',
                        headers=header)

item = response.text

soup = BeautifulSoup(item, features="lxml")
price = soup.find(name='span', class_="a-size-base-plus a-color-price bundle-price-base a-text-bold").get_text()
price = float(price.split('₹')[1])

if price <= expected:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="pavankpawankpavan@gmail.com",
                        msg=f"Subject: price lower than expected \n\nthe price of your product is less than {expected} you can make a purchase")
