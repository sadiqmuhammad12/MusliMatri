from pageObject.pages.basePage import basePage
from pageObject.pages.locators.signupLocators.signupLocators import signupLocators
from pageObject.config.signup import signupTestData
import time

class signupPage(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(signupTestData.base_url)

    def do_signup(self, first_name, last_name, date_of_birth, email, password, confirm_password, phone_number):
        self.do_click(signupLocators.search_for)
        time.sleep(2)
        self.do_click(signupLocators.value_search_for)
        time.sleep(2)
        self.do_click(signupLocators.age_from)
        time.sleep(2)

        self.do_click(signupLocators.value_age_from)
        time.sleep(2)

        self.do_click(signupLocators.age_to)
        time.sleep(2)

        self.do_click(signupLocators.value_age_to)
        time.sleep(2)

        self.do_click(signupLocators.my_disability)
        time.sleep(2)

        self.do_click(signupLocators.value_my_disability)
        time.sleep(2)

        self.do_click(signupLocators.search_btn)
        time.sleep(2)

        #for profile and gender Section
        self.do_click(signupLocators.my_self)
        time.sleep(2)

        self.do_click(signupLocators.male)
        time.sleep(2)

        self.do_click(signupLocators.salutation)
        time.sleep(2)

        self.do_click(signupLocators.value_salutation)
        time.sleep(2)

        self.do_send_keys(signupLocators.first_name, first_name)
        time.sleep(1)
        self.do_send_keys(signupLocators.last_name, last_name)
        time.sleep(2)
        #DOB
        self.do_send_keys(signupLocators.date_of_birth, date_of_birth)
        time.sleep(2)

        self.do_click(signupLocators.next_btns)
        time.sleep(2)

        # nationality
        self.do_click(signupLocators.nationality)
        time.sleep(2)

        self.do_click(signupLocators.value_nationality)

        self.do_click(signupLocators.religion)
        time.sleep(2)

        self.do_click(signupLocators.value_religion)


        self.do_click(signupLocators.language)
        time.sleep(2)

        self.do_click(signupLocators.value_language)
        time.sleep(2)

        self.do_click(signupLocators.next_btn)
        time.sleep(2)

        self.do_send_keys(signupLocators.email, email)
        time.sleep(2)

        self.do_send_keys(signupLocators.password, password)
        time.sleep(2)

        self.do_send_keys(signupLocators.confirm_password, confirm_password)
        time.sleep(2)

        self.do_send_keys(signupLocators.phone_number, phone_number)
        time.sleep(2)

        self.do_click(signupLocators.submit_btn)
        time.sleep(2)
