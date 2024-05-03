import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.login import testData
from pageObject.pages.loginPage import loginPage
from pageObject.pages.locators.loginPageLocators.loginPageLocators import locators


def test_login():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.email, testData.password)

        time.sleep(6)

        # get the current URL of the page
        current_url = driver.current_url
        # check if the expected text is in the URL
        if "matching" in current_url:
            print("User is logged in and redirected to the Matching page")
        else:
            print("User login failed or was not redirected to the Matching page")

        # close the web driver instance
        driver.quit()
    except Exception as e:
        print("An error occurred:", e)


# if __name__ == "__main__":
#     main()
