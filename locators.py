from selenium.webdriver.common.by import By

class RegistrationLocators:
    # Static locators; these are not initialized until called in methods
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    PASSWORD_CONFIRMATION = (By.ID, 'password-confirmation')
    SUBMIT_BUTTON = (By.XPATH, '//*[@id="form-validate"]/div/div[1]/button')
    EXPECTED_TEXT = (By.XPATH, '//*[@id="maincontent"]/div[1]/div[2]/div/div/div')
