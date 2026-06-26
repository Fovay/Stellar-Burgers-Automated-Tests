from selenium.webdriver.common.by import By

class ProfileLocators:

    personal_account_button = (By.XPATH,"//p[text()='Личный Кабинет']")
    constructor_button = (By.XPATH,"//p[text()='Конструктор']")
    logo_button = (By.XPATH,"//a[contains(@href,'/')]")
    logout_button = (By.XPATH,"//button[text()='Выход']")