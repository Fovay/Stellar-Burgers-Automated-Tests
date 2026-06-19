from generations import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def authorize(driver):
    driver.get(URL + 'login')
    driver.find_element('xpath', "//input[@name='name']").send_keys(Test_email)
    driver.find_element('xpath',"//input[@type='password']").send_keys(Test_password)
    driver.find_element('xpath',"//button[text()='Войти']").click()

def test_go_to_personal_account(driver):
    driver.get(URL)
    driver.find_element('xpath',"//p[text()='Личный Кабинет']").click()
    assert 'login' in driver.current_url

def test_go_to_constructor(driver):
    driver.get(URL)
    driver.find_element('xpath',"//p[text()='Личный Кабинет']").click()
    driver.find_element('xpath',"//p[text()='Конструктор']").click()
    assert driver.current_url == URL

def test_go_to_constructor_by_logo(driver):
    driver.get(URL)
    driver.find_element('xpath',"//p[text()='Личный Кабинет']").click()
    driver.find_element('xpath',"//a[contains(@href,'/')]").click()
    assert driver.current_url == URL


def test_logout(driver):
    authorize(driver)
    driver.find_element('xpath', "//p[text()='Личный Кабинет']").click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
    driver.find_element('xpath', "//button[text()='Выход']").click()
    WebDriverWait(driver, 5).until(EC.url_contains("login"))