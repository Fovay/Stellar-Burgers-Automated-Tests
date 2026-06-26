from selenium.webdriver.common.by import By

class RegistrationLocators:

    name_input = (By.XPATH,"//input[@name='name']")
    email_input = (By.XPATH,"//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH,"//input[@type='password']")

    register_button = (By.XPATH,"//button[text()='Зарегистрироваться']")

    password_error = (By.XPATH,"//*[contains(text(),'Некорректный пароль')]")