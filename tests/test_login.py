from data.urls import Urls
from data.test_data import UserData
from pages.login_page import LoginPage
from locators.login_locators import LoginLocators

class TestLogin:
    
    def test_login_from_main_page(self, driver):
        driver.get(Urls.base_url)
        driver.find_element(*LoginLocators.main_login_button).click()
        login_page = LoginPage(driver)
        login_page.login(UserData.email, UserData.password)
        assert "login" not in driver.current_url

    def test_login_from_personal_account(self, driver):
        driver.get(Urls.base_url)
        driver.find_element(*LoginLocators.personal_account_button).click()
        login_page = LoginPage(driver)
        login_page.login(UserData.email, UserData.password)
        assert "login" not in driver.current_url

    def test_login_from_registration_page(self, driver):
        driver.get(Urls.register_url)
        driver.find_element(*LoginLocators.register_login_link).click()
        login_page = LoginPage(driver)
        login_page.login(UserData.email, UserData.password)
        assert "login" not in driver.current_url

    def test_login_from_forgot_password_page(self, driver):
        driver.get(Urls.login_url)
        driver.find_element(*LoginLocators.forgot_password_link).click()
        driver.find_element(*LoginLocators.register_login_link).click()
        login_page = LoginPage(driver)
        login_page.login(UserData.email, UserData.password)
        assert "login" not in driver.current_url