from selenium import webdriver
from actions import RegistrationPage

def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/customer/account/create/")
    driver.maximize_window()

    registration_page = RegistrationPage(driver)
    registration_page.enter_details("Tamar", "Abramishvili", "tamadaaaaaddraaaaalllllaaaaaaaaaaa@gmail.com", "Tamara.5", "Tamara.5")
    registration_page.submit_form()

    actual_result = registration_page.get_confirmation_message()
    print(actual_result)
    expected_result = "Thank you for registering with Main Website Store."
    assert expected_result in actual_result

    driver.quit()
