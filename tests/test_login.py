from generations import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def login(driver):
    driver.find_element('xpath', "//input[@name='name']").send_keys(Test_email)
    driver.find_element('xpath', "//input[@type='password']").send_keys(Test_password)
    driver.find_element('xpath', "//button[text()='Войти']").click()
    WebDriverWait(driver, 5).until(EC.url_changes("https://stellarburgers.education-services.ru/login"))

def test_login_from_main_page(driver):
    driver.get(URL)
    driver.find_element('xpath',"//button[text()='Войти в аккаунт']").click()
    login(driver)
    assert 'login' not in driver.current_url

def test_login_from_personal_account(driver):
    driver.get(URL)
    driver.find_element('xpath',"//p[text()='Личный Кабинет']").click()
    login(driver)
    assert 'login' not in driver.current_url

def test_login_from_registration_page(driver):
    driver.get(URL + 'register')
    driver.find_element('link text','Войти').click()
    login(driver)
    assert 'login' not in driver.current_url

def test_login_from_forgot_password_page(driver):
    driver.get(URL + 'login')
    driver.find_element('link text','Восстановить пароль').click()
    driver.find_element('link text','Войти').click()
    login(driver)
    assert 'login' not in driver.current_url