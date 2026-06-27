from pages.base_page import BasePage
from locators.login_locators import LoginLocators
from data.urls import Urls


class LoginPage(BasePage):

    def click_main_login_button(self):
        self.click_element(LoginLocators.main_login_button)

    def click_personal_account_button(self):
        self.click_element(LoginLocators.personal_account_button)

    def click_register_login_link(self):
        self.click_element(LoginLocators.register_login_link)

    def click_forgot_password_link(self):
        self.click_element(LoginLocators.forgot_password_link)

    def login(self, email, password):
        self.send_keys(LoginLocators.email_input, email)
        self.send_keys(LoginLocators.password_input, password)
        self.click_element(LoginLocators.login_button)
        self.wait_url_change(Urls.login_url)