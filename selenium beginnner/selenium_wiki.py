from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge()
driver.get('https://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.NAME, 'fName')
lname = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
signup = driver.find_element(By.CLASS_NAME, "btn-block")

fname.send_keys('Rohit')
lname.send_keys('Sharma')
email.send_keys('HEYEHEYYEYE@gmail.com')
signup.click()
driver.quit()
# search_bar = driver.find_element(By.NAME, 'search')
# search_bar.send_keys('Python')
# search_bar.send_keys(Keys.ENTER)
