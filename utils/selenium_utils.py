import time
from selenium.common.exceptions import NoSuchElementException


class SeleniumUtils():

    def wait_until_element_found(self, by_locator=None, delay=5):
        count = 0
        while count < delay:
            count = count + 1
            try:
                self.driver.find_element(*by_locator)
                return self
            except NoSuchElementException:
                time.sleep(1)
        return self
