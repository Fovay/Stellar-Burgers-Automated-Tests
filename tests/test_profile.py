from data.urls import Urls
from data.test_data import UserData
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

class TestProfile:

    def test_go_to_personal_account(self, driver):
        driver.get(Urls.login_url)
        login_page = LoginPage(driver)
        login_page.login(UserData.email, UserData.password)
        profile_page = ProfilePage(driver)
        profile_page.open_personal_account()
        assert "/account" in driver.current_url

    def test_go_to_constructor(self, driver):
        driver.get(Urls.login_url)
        login_page = LoginPage(driver)
        login_page.login(UserData.email, UserData.password)
        profile_page = ProfilePage(driver)
        profile_page.open_personal_account()
        profile_page.open_constructor()
        assert driver.current_url == Urls.base_url

    def test_go_to_constructor_by_logo(self, driver):
        driver.get(Urls.login_url)
        login_page = LoginPage(driver)
        login_page.login(UserData.email, UserData.password)
        profile_page = ProfilePage(driver)
        profile_page.open_personal_account()
        profile_page.open_constructor_by_logo()
        assert driver.current_url == Urls.base_url

    def test_logout(self, driver):
        driver.get(Urls.login_url)
        login_page = LoginPage(driver)
        login_page.login(UserData.email, UserData.password)
        profile_page = ProfilePage(driver)
        profile_page.open_personal_account()
        profile_page.logout()
        assert "login" in driver.current_url