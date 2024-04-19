from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationLocators
import time
class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(2)

    def enter_details(self, first_name, last_name, email, password, confirmation):
        self.driver.find_element(*RegistrationLocators.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*RegistrationLocators.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*RegistrationLocators.EMAIL).send_keys(email)
        self.driver.find_element(*RegistrationLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*RegistrationLocators.PASSWORD_CONFIRMATION).send_keys(confirmation)

    def submit_form(self):
        self.driver.find_element(*RegistrationLocators.SUBMIT_BUTTON).click()

    def get_confirmation_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.EXPECTED_TEXT)
        )
        return element.text
