from pageObject.pages.basePage import basePage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators
from pageObject.config.login import testData


class loginPage(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(testData.base_url)

    def do_login(self, email, password):
        self.do_click(locators.login)
        self.do_send_keys(locators.email, email)
        self.do_send_keys(locators.password, password)
        self.do_click(locators.login_btn)
