from pages.constructor_page import ConstructorPage
from data.urls import Urls


class TestConstructor:

    def test_bun_tab_active_by_default(self, driver):
        page = ConstructorPage(driver)
        page.open_url(Urls.base_url)
        assert page.is_bun_tab_active()

    def test_sauce_tab_scrolls_to_category(self, driver):
        page = ConstructorPage(driver)
        page.open_url(Urls.base_url)
        page.switch_to_sauce_tab()
        assert page.is_sauce_tab_active()

    def test_filling_tab_scrolls_to_category(self, driver):
        page = ConstructorPage(driver)
        page.open_url(Urls.base_url)
        page.switch_to_filling_tab()
        assert page.is_filling_tab_active()