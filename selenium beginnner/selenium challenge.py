from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.python.org/")
li2=[]
event = driver.find_element(By.XPATH, '/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul')
li = event.text.split("\n")
print(li)

for i in range(len(li)):
    li2.append(i)
d = dict(zip(li2, li))
print(d)

