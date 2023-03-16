from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.Locators.Login import LogIn

login = LogIn()


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        username_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, login.user_name_field)))
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, login.password_field)))
        password_field.send_keys(password)

    def click_login(self):
        login_field = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, login.login_btn)))
        login_field.click()
