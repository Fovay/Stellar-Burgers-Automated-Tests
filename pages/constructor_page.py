from pages.base_page import BasePage
from locators.constructor_locators import ConstructorLocators
from data.constructor_data import TabsData


class ConstructorPage(BasePage):

    def _is_bun_tab_active(self):
        classes = self.get_attribute(ConstructorLocators.bun_tab, "class").split()
        return any(TabsData.active_tab_class in cls for cls in classes)

    def _is_sauce_tab_active(self):
        classes = self.get_attribute(ConstructorLocators.sauce_tab, "class").split()
        return any(TabsData.active_tab_class in cls for cls in classes)

    def _is_filling_tab_active(self):
        classes = self.get_attribute(ConstructorLocators.filling_tab, "class").split()
        return any(TabsData.active_tab_class in cls for cls in classes)

    def _switch_to_tab(self, tab_locator, header_locator):
        self.click_element(tab_locator)
        self.scroll_to_element(header_locator)

    def switch_to_bun_tab(self):
        self._switch_to_tab(ConstructorLocators.bun_tab, ConstructorLocators.bun_header)

    def switch_to_sauce_tab(self):
        self._switch_to_tab(ConstructorLocators.sauce_tab, ConstructorLocators.sauce_header)

    def switch_to_filling_tab(self):
        self._switch_to_tab(ConstructorLocators.filling_tab, ConstructorLocators.filling_header)

    def is_bun_tab_active(self):
        return self._is_bun_tab_active()

    def is_sauce_tab_active(self):
        return self._is_sauce_tab_active()

    def is_filling_tab_active(self):
        return self._is_filling_tab_active()