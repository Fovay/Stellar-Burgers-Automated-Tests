from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from data.urls import Urls
from data.test_data import UserData


class TestProfile:

    def test_go_to_personal_account(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Urls.login_url)
        login_page.login(UserData.email, UserData.password)
        profile_page = ProfilePage(driver)
        profile_page.open_personal_account()
        assert "/account" in profile_page.get_current_url()

    def test_go_to_constructor(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Urls.login_url)
        login_page.login(UserData.email, UserData.password)
        profile_page = ProfilePage(driver)
        profile_page.open_personal_account()
        profile_page.open_constructor()
        assert profile_page.get_current_url() == Urls.base_url

    def test_go_to_constructor_by_logo(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Urls.login_url)
        login_page.login(UserData.email, UserData.password)
        profile_page = ProfilePage(driver)
        profile_page.open_personal_account()
        profile_page.open_constructor_by_logo()
        assert profile_page.get_current_url() == Urls.base_url

    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Urls.login_url)
        login_page.login(UserData.email, UserData.password)
        profile_page = ProfilePage(driver)
        profile_page.open_personal_account()
        profile_page.logout()
        assert "login" in profile_page.get_current_url()