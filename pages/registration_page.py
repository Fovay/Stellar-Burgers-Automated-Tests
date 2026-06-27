from pages.base_page import BasePage
from locators.registration_locators import RegistrationLocators
from data.urls import Urls


class RegistrationPage(BasePage):

    def register(self, name, email, password):
        self.send_keys(RegistrationLocators.name_input, name)
        self.send_keys(RegistrationLocators.email_input, email)
        self.send_keys(RegistrationLocators.password_input, password)
        self.click_element(RegistrationLocators.register_button)

    def wait_registration_success(self):
        self.wait_url_change(Urls.register_url)

    def get_password_error(self):
        return self.wait_visible(RegistrationLocators.password_error)