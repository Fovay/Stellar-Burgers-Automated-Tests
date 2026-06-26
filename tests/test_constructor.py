from data.urls import Urls
from pages.constructor_page import ConstructorPage

class TestConstructor:

    def test_bun_tab_valid_working(self, driver):
        driver.get(Urls.base_url)
        page = ConstructorPage(driver)
        assert page.is_bun_tab_active()

    def test_sauce_tab_valid_working(self, driver):
        driver.get(Urls.base_url)
        page = ConstructorPage(driver)
        page.switch_to_sauce_tab()
        assert page.is_sauce_tab_active()

    def test_filling_tab_valid_working(self, driver):
        driver.get(Urls.base_url)
        page = ConstructorPage(driver)
        page.switch_to_filling_tab()
        assert page.is_filling_tab_active()