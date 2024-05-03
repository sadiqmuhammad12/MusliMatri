from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class basePage:
    """it contains all the generic method and utilities"""

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        send_value = (WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)))
        send_value.clear()
        send_value.send_keys(text)
