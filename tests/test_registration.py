from data.urls import Urls
from data.test_data import UserData
from generators import generate_email
from pages.registration_page import RegistrationPage

class TestRegistration:

    def test_register_user_successfully(self, driver):
        driver.get(Urls.register_url)
        registration_page = RegistrationPage(driver)
        registration_page.register(UserData.name,generate_email(),UserData.password)
        registration_page.wait_registration_success()
        assert "login" in driver.current_url

    def test_register_user_with_short_password(self, driver):
        driver.get(Urls.register_url)
        registration_page = RegistrationPage(driver)
        registration_page.register(UserData.name,generate_email(),"123")
        error = registration_page.get_password_error()
        assert error.is_displayed()