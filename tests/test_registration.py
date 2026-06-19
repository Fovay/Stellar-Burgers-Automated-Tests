from generations import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_register_user_successfully(driver):
    driver.get(URL + 'register')
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys('Анастасия')
    email_input = "//label[text()='Email']/following-sibling::input"
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, email_input)))
    driver.find_element(By.XPATH, email_input).send_keys(generate_email())
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123456')
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    WebDriverWait(driver, 5).until(EC.url_changes(URL + 'register'))
    
def test_register_user_with_short_password(driver):
    driver.get(URL + 'register')
    driver.find_element(By.XPATH, "//input[@name='name']").send_keys('Анастасия')
    email_input = "//label[text()='Email']/following-sibling::input"
    driver.find_element(By.XPATH, email_input).send_keys(generate_email())
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys('123')
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()
    error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Некорректный пароль')]")))
    assert error.is_displayed()