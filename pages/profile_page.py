from pages.base_page import BasePage
from locators.profile_locators import ProfileLocators


class ProfilePage(BasePage):

    def open_personal_account(self):
        self.click_element(ProfileLocators.personal_account_button)

    def open_constructor(self):
        self.click_element(ProfileLocators.constructor_button)

    def open_constructor_by_logo(self):
        self.click_element(ProfileLocators.logo_button)

    def logout(self):
        self.wait_visible(ProfileLocators.logout_button)
        self.click_element(ProfileLocators.logout_button)
        self.wait_url_contains("login")