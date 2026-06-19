from generations import URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_bun_tab_valid_working(driver):
    driver.get(URL)
    assert driver.find_element('xpath',"//span[text()='Булки']").is_displayed()

def test_sauce_tab_valid_working(driver):
    driver.get(URL)
    driver.find_element('xpath',"//span[text()='Соусы']").click()
    assert driver.find_element('xpath',"//span[text()='Соусы']").is_displayed()
    
def test_filling_tab_valid_working(driver):
    driver.get(URL)
    driver.find_element('xpath',"//span[text()='Начинки']").click()
    assert driver.find_element('xpath',"//span[text()='Начинки']").is_displayed()