import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('http://orteil.dashnet.org/experiments/cookie/')

timeout = time.time()+5
five_min = time.time()+60*5

cookie_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[6]/div[9]')
your_money = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]')
while True:
    cookie_button.click()

    if time.time() > timeout:
        allprice = driver.find_elements(By.CSS_SELECTOR, '#store b')
        for price in allprice:
            if price.text != "":
                item_prices = []
                cost = int(price.text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)


