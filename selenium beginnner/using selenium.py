from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = "D:\dev\chromedriver-win64"
driver = webdriver.Edge()
driver.get('https://www.python.org/')
search_bar = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")#in a class of doc widget
                                                                                 # and find anchor tag

print(driver.find_element(By.XPATH, value='//*[@id="submit"]'))
print(search_bar.text)

driver.quit()
