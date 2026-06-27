from selenium.webdriver.common.by import By

class LoginLocators:

    email_input = (By.XPATH,"//input[@name='name']")
    password_input = (By.XPATH,"//input[@type='password']")
    
    login_button = (By.XPATH,"//button[text()='Войти']")
    personal_account_button = (By.XPATH,"//p[text()='Личный Кабинет']")
    main_login_button = (By.XPATH,"//button[text()='Войти в аккаунт']")
    
    register_login_link = (By.LINK_TEXT,"Войти")
    forgot_password_link = (By.LINK_TEXT,"Восстановить пароль")