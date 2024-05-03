from selenium.webdriver.common.by import By


class completeProfileLocators:
    complete_profile_btn = (By.ID, "CPless35")

    #background Page
    education = (By.ID, 'educationId')
    value_education = (By.XPATH, '//*[@id="educationId"]/option[7]')
    ethnicity = (By.ID, 'ethnicityId')
    value_ethnicity = (By.XPATH, '//*[@id="ethnicityId"]/option[7]')
    religious_practices = (By.ID, 'religiousServicesId')
    value_religious_practices = (By.XPATH, '//*[@id="religiousServicesId"]/option[2]')
    faith_status = (By.ID, 'bornRevertId')
    value_faith_status = (By.XPATH, '//*[@id="bornRevertId"]/option[2]')
    disability = (By.ID, 'disabilityId')
    value_disability = (By.XPATH, '//*[@id="disabilityId"]/option[16]')
    merital_status = (By.ID, 'maritalStatusId')
    value_merital_status = (By.XPATH, '//*[@id="maritalStatusId"]/option[3]')
    ambition_goal = (By.ID, 'ambitionGoals')
    upload_your_profile_photo_btn = (By.CLASS_NAME, 'custom-file-label1')
    next_btn = (By.CSS_SELECTOR, "button[type='button']")

