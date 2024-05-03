from selenium.webdriver.common.by import By


class locators:
    login = (By.XPATH, "//a[@href='/Identity/Account/Login']")
    email = (By.ID, 'Input_Email')
    password = (By.ID, 'txtPassword')
    login_btn = (By.CLASS_NAME, 'btn')