import time
import chromedriver_autoinstaller
from selenium import webdriver
from pageObject.config.completeProfile import completeProfileTestData
from pageObject.pages.completeProfilePage import completeProfile
from pageObject.config.login import testData
from pageObject.pages.loginPage import loginPage

def pause_test():
    input("Please perform necessary actions manually. Press Enter to continue...")


def test_completeProfile():
    try:
        chromedriver_autoinstaller.install()

        driver = webdriver.Chrome()
        driver.maximize_window()

        login_page = loginPage(driver)
        login_page.do_login(testData.email, testData.password)
        time.sleep(6)
        complete_profile_page = completeProfile(driver)
        complete_profile_page.do_complete_profile(completeProfileTestData.ambition_goal)
        complete_profile_page.do_complete_profile(completeProfileTestData.upload_your_profile_photo_btn)


        # get the current URL of the page
        #current_url = driver.current_url
        # # check if the expected text is in the URL
        #if "upload-your-profile-photo" in current_url:
            pause_test()
            time.sleep(6)
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

