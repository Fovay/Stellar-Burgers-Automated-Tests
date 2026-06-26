from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registration_locators import RegistrationLocators
from data.urls import Urls

class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver

    def register(self, name, email, password):
        self.driver.find_element(*RegistrationLocators.name_input).send_keys(name)
        self.driver.find_element(*RegistrationLocators.email_input).send_keys(email)
        self.driver.find_element(*RegistrationLocators.password_input).send_keys(password)
        self.driver.find_element(*RegistrationLocators.register_button).click()

    def wait_registration_success(self):
        WebDriverWait(self.driver, 10).until(EC.url_changes(Urls.register_url))

    def get_password_error(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(RegistrationLocators.password_error))