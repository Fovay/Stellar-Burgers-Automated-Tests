from pages.login_page import LoginPage
from data.urls import Urls
from data.test_data import UserData


class TestLogin:

    def test_login_from_main_page(self, driver):
        page = LoginPage(driver)
        page.open_url(Urls.base_url)
        page.click_main_login_button()
        page.login(UserData.email, UserData.password)
        assert "login" not in page.get_current_url()

    def test_login_from_personal_account(self, driver):
        page = LoginPage(driver)
        page.open_url(Urls.base_url)
        page.click_personal_account_button()
        page.login(UserData.email, UserData.password)
        assert "login" not in page.get_current_url()

    def test_login_from_registration_page(self, driver):
        page = LoginPage(driver)
        page.open_url(Urls.register_url)
        page.click_register_login_link()
        page.login(UserData.email, UserData.password)
        assert "login" not in page.get_current_url()

    def test_login_from_forgot_password_page(self, driver):
        page = LoginPage(driver)
        page.open_url(Urls.login_url)
        page.click_forgot_password_link()
        page.click_register_login_link()
        page.login(UserData.email, UserData.password)
        assert "login" not in page.get_current_url()