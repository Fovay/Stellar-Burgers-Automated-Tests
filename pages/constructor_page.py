import time
from selenium.webdriver.support.ui import WebDriverWait
from locators.constructor_locators import ConstructorLocators
from data.constructor_data import TabsData

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        
    def _is_tab_active(self, tab_locator):
        element = self.driver.find_element(*tab_locator)
        classes = element.get_attribute("class").split()
        return any(TabsData.active_tab_class in cls for cls in classes)

    def _switch_to_tab(self, tab_locator, header_locator):
        element = self.driver.find_element(*tab_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'instant', block: 'center'});", element)
        time.sleep(0.5)
        element.click()
        WebDriverWait(self.driver, 5).until(lambda d: self._is_tab_active(tab_locator))
        header = self.driver.find_element(*header_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'start'});", header)
        time.sleep(1)
        WebDriverWait(self.driver, 5).until(lambda d: d.execute_script("""var rect = arguments[0].getBoundingClientRect();return rect.top >= 80 && rect.bottom <= window.innerHeight;""", header))

    def switch_to_bun_tab(self):
        self._switch_to_tab(ConstructorLocators.bun_tab, ConstructorLocators.bun_header)

    def switch_to_sauce_tab(self):
        self._switch_to_tab(ConstructorLocators.sauce_tab, ConstructorLocators.sauce_header)

    def switch_to_filling_tab(self):
        self._switch_to_tab(ConstructorLocators.filling_tab, ConstructorLocators.filling_header)

    def is_bun_tab_active(self):
        return self._is_tab_active(ConstructorLocators.bun_tab)

    def is_sauce_tab_active(self):
        return self._is_tab_active(ConstructorLocators.sauce_tab)

    def is_filling_tab_active(self):
        return self._is_tab_active(ConstructorLocators.filling_tab)