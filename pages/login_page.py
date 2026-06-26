from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from data.urls import Urls

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(*LoginLocators.email_input).send_keys(email)
        self.driver.find_element(*LoginLocators.password_input).send_keys(password)
        self.driver.find_element(*LoginLocators.login_button).click()
        WebDriverWait(self.driver, 5).until(EC.url_changes(Urls.login_url))