import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from data.constants import Constants


class DriverSetup():

    @classmethod
    def setUpClass(cls):
        DRIVER_PATH = os.getenv('DRIVER_PATH', '/Library/ChromeDriver/chromedriver')
        cls.driver = webdriver.Chrome(
            '/Library/ChromeDriver/chromedriver')
        cls.wait = WebDriverWait(cls.driver, 4)

    def setUp(self):
        self.driver.get(Constants.BASE_URL)

    def tearDown(self):
        self.driver.quit()
