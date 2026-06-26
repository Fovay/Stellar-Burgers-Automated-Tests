from selenium.webdriver.common.by import By

class ConstructorLocators:
    bun_tab = (By.XPATH, "//span[text()='Булки']/parent::*")
    sauce_tab = (By.XPATH, "//span[text()='Соусы']/parent::*")
    filling_tab = (By.XPATH, "//span[text()='Начинки']/parent::*")

    bun_header = (By.XPATH, "//h2[text()='Булки']")
    sauce_header = (By.XPATH, "//h2[text()='Соусы']")
    filling_header = (By.XPATH, "//h2[text()='Начинки']")