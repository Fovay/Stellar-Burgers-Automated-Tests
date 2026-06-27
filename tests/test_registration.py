from pages.registration_page import RegistrationPage
from data.urls import Urls
from data.test_data import UserData
from generators import generate_email


class TestRegistration:

    def test_register_user_successfully(self, driver):
        page = RegistrationPage(driver)
        page.open_url(Urls.register_url)
        page.register(UserData.name, generate_email(), UserData.password)
        page.wait_registration_success()
        assert "login" in page.get_current_url()

    def test_register_user_with_short_password(self, driver):
        page = RegistrationPage(driver)
        page.open_url(Urls.register_url)
        page.register(UserData.name, generate_email(), "123")
        error = page.get_password_error()
        assert error.is_displayed()