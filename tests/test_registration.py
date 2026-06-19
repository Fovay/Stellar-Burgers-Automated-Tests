from generations import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_register_user_successfully(driver):
    driver.get(URL + 'register')
    driver.find_element('xpath', "//input[@name='name']").send_keys('Анастасия')
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input")))
    driver.find_element('xpath',"//label[text()='Email']/following-sibling::input").send_keys(generate_email())
    driver.find_element('xpath', "//input[@type='password']").send_keys('123456')
    driver.find_element('xpath', "//button[text()='Зарегистрироваться']").click()
    
def test_register_user_with_short_password(driver):
    driver.get(URL + 'register')
    driver.find_element('xpath', "//input[@name='name']").send_keys('Анастасия')
    driver.find_element('xpath',"//label[text()='Email']/following-sibling::input").send_keys(generate_email())
    driver.find_element('xpath', "//input[@type='password']").send_keys('123')
    driver.find_element('xpath', "//button[text()='Зарегистрироваться']").click()
    assert driver.find_element('xpath',"//*[contains(text(),'Некорректный пароль')]").is_displayed()