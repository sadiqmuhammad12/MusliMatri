from selenium.webdriver.common.by import By


class signupLocators:
    search_for = (By.CLASS_NAME, "form-control.homeGender.px-2")
    value_search_for = (By.XPATH, '//*[@id="header"]/div/div[2]/div/div[1]/div/select/option[2]')
    age_from = (By.CLASS_NAME, "form-control.homeAgeFrom.px-2")
    value_age_from = (By.XPATH, '//*[@id="ageId"]/option[2]')
    age_to = (By.CLASS_NAME, 'form-control.homeAgeTo.px-2')
    value_age_to = (By.XPATH, '/html/body/header/div/div[2]/div/div[3]/div/select/option[4]')
    my_disability = (By.ID, 'disabilityId')
    value_my_disability = (By.XPATH, '//*[@id="disabilityId"]/option[16]')
    search_btn = (By.CLASS_NAME, 'btn.form-control.search-style.golden-harvest-bg')

    #for profile Section
    my_self = (By.XPATH, '//*[@id="step-1"]/div/div[2]/div/div[1]/label[1]')

    #dependent gender
    male = (By.XPATH, '//*[@id="active-display"]/div/label[2]')

    #profile name Section
    salutation = (By.ID, 'salutaionId')
    value_salutation = (By.XPATH, '//*[@id="salutaionId"]/option[2]')

    first_name = (By.ID, 'firstName')
    last_name = (By.ID, 'lastName')

    #date of Birth
    date_of_birth = (By.ID,'dob')

    next_btns = (By.XPATH, '//*[@id="msform"]/div[3]/button[2]')

    # Nationality Page
    nationality = (By.XPATH, '/html/body/div[4]/div/div/div/div/section[4]/div/div[2]/div[1]/select[1]')
    # value_nationality = (By.XPATH, '//*[@id="nationalityId"]/option[2]')
    value_nationality = (By.XPATH, '/html/body/div[4]/div/div/div/div/section[4]/div/div[2]/div[1]/select[1]/option[2]')
    religion = (By.XPATH, '//*[@id="religionId"]')
    value_religion = (By.XPATH, '//*[@id="religionId"]/option[2]')

    language = (By.ID,'languageSpokenId')
    value_language = (By.XPATH, '//*[@id="languageSpokenId"]/option[125]')

    next_btn = (By.XPATH, '//*[@id="step-3"]/div/div[2]/div[2]/button[2]')
    #
    # email,password, confirm password,, Phone Number
    email = (By.ID, 'Email')
    password = (By.ID, 'Password')
    confirm_password = (By.ID, 'ConfirmPassword')
    phone_number = (By.ID, 'PhoneNumber')

    submit_btn = (By.ID, 'createprofileForm')

