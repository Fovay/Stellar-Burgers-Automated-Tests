from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'start'});",element)

    def wait_url_change(self, old_url):WebDriverWait(self.driver, 10).until(EC.url_changes(old_url))

    def wait_url_contains(self, text):WebDriverWait(self.driver, 10).until(EC.url_contains(text))

    def wait_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url):
        self.driver.get(url)