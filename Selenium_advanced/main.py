from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.freepik.com/free-photos-vectors/website-button")
driver.implicitly_wait(3)
button = driver.find_element("xpath", '/html/body/main/div[2]/div[3]/div/ul/li[1]/a')
button.click()

