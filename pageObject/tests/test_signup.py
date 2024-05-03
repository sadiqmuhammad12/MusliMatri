import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.signup import signupTestData
from pageObject.pages.signupPage import signupPage
from pageObject.pages.locators.signupLocators.signupLocators import signupLocators

def test_signup():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        signup_page = signupPage(driver)
        signup_page.do_signup(signupTestData.first_name, signupTestData.last_name, signupTestData.date_of_birth,signupTestData.email,signupTestData.password,signupTestData.confirm_password,signupTestData.phone_number)

        time.sleep(6)

        # get the current URL of the page
        # current_url = driver.current_url
        # # check if the expected text is in the URL
        # if "matching" in current_url:
        #     print("User is logged in and redirected to the Matching page")
        # else:
        #     print("User login failed or was not redirected to the Matching page")

        # close the web driver instance
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)
    # finally:
    #     driver.quit()


# if __name__ == "__main__":
#     main()

