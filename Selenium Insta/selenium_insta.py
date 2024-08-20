import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import ElementClickInterceptedException
driver = webdriver.Edge()
driver.get('https://www.instagram.com/?hl=en')

msg1 = ['<3', '♥']
msg2 = f'{random.choice(msg1)}'

username = driver.find_element(By.NAME, 'username')
username.send_keys('pavankpawankpavan@gmail.com')
password = driver.find_element(By.NAME,'password')
password.send_keys(os.getenv('PASSWORD'))
password.send_keys(Keys.ENTER)
time.sleep(7)

not_now = driver.find_element(By.CSS_SELECTOR, '._ac8f div')
not_now.click()
time.sleep(4)

driver.get(os.getenv('ADDRESS'))
time.sleep(3)
msg = driver.find_element(By.CSS_SELECTOR, '.x1n2onr6 .focus-visible')
for i in range(3):
    time.sleep(2)
    msg.send_keys(f'{random.choice(msg2)} {random.choice(msg1)}')
    msg.send_keys(Keys.ENTER)
