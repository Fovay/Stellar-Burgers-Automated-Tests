from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.profile_locators import ProfileLocators

class ProfilePage:

    def __init__(self, driver):
        self.driver = driver

    def open_personal_account(self):
        self.driver.find_element(*ProfileLocators.personal_account_button).click()

    def open_constructor(self):
        self.driver.find_element(*ProfileLocators.constructor_button).click()

    def open_constructor_by_logo(self):
        self.driver.find_element(*ProfileLocators.logo_button).click()

    def logout(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ProfileLocators.logout_button))
        self.driver.find_element(*ProfileLocators.logout_button).click()
        WebDriverWait(self.driver, 5).until(EC.url_contains("login"))