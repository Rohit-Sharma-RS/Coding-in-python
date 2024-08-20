import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/home')

username = driver.find_element(By.ID, 'session_key')
username.send_keys('rohitlolwr@gmail.com')

password = driver.find_element(By.NAME, 'session_password')
password.send_keys('your linked in password')

signin = driver.find_element(By.XPATH, '/html/body/main/section[1]/div/div/form/div[2]/button')
signin.click()

time.sleep(45)  # clear captcha

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(2)

jobs_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in jobs_list:
    time.sleep(1)
    job.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button").click()
        time.sleep(2)

        submit_button = driver.find_element(By.CSS_SELECTOR, ".justify-flex-end button .artdeco-button__text")
        # if submit button is available in page only than fill the form, otherwise it has multi steps to fill form.
        if submit_button.text == 'Submit application':
            add_number = driver.find_element(By.CSS_SELECTOR, '.fb-single-line-text input')
            # check if the text field is empty, only then enter your number
            if add_number.get_attribute("value") == "":
                add_number.send_keys('8403984747')
            submit_button.click()
            print('Applied')
            time.sleep(5)

        if submit_button.get_attribute('aria-label') == "Continue to next step":
            close = driver.find_element(By.CLASS_NAME, 'artdeco-modal__dismiss')
            close.click()
            discard = driver.find_elements(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')[1]
            discard.click()
            print("Complex so skipped")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print('no button found')
        continue
time.sleep(5)
driver.quit()
