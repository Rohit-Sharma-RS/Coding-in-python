from selenium import webdriver
import os
import constants
class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\chromedriver\chromedriver.exe"):
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(constants.BASE_URL)
