from pageObject.pages.basePage import basePage
from pageObject.pages.locators.completeProfileLocators.completeProfileLocators import completeProfileLocators
from pageObject.config.completeProfile import completeProfileTestData
import time

class completeProfile(basePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(signupTestData.base_url)

    def do_complete_profile(self, ambition_goal):
        self.do_click(completeProfileLocators.complete_profile_btn)
        time.sleep(2)

        #Background Page
        self.do_click(completeProfileLocators.education)
        self.do_click(completeProfileLocators.value_education)
        time.sleep(2)

        self.do_click(completeProfileLocators.ethnicity)
        self.do_click(completeProfileLocators.value_ethnicity)
        time.sleep(2)

        self.do_click(completeProfileLocators.religious_practices)
        self.do_click(completeProfileLocators.value_religious_practices)
        # time.sleep(2)

        self.do_click(completeProfileLocators.faith_status)
        self.do_click(completeProfileLocators.value_faith_status)
        # time.sleep(2)

        self.do_click(completeProfileLocators.disability)
        self.do_click(completeProfileLocators.value_disability)
        # time.sleep(2)

        self.do_click(completeProfileLocators.merital_status)
        self.do_click(completeProfileLocators.value_merital_status)
        # time.sleep(2)

        self.do_send_keys(completeProfileLocators.ambition_goal, ambition_goal)
        # time.sleep(2)

        self.do_click(completeProfileLocators.upload_your_profile_photo_btn)
        time.sleep(5)
        self.do_send_keys(completeProfileLocators.upload_your_profile_photo_btn, file_path)

        # self.do_send_keys(completeProfileTestData.file_path)
        time.sleep(2)

        self.do_click(completeProfileLocators.next_btn)
        time.sleep(3)