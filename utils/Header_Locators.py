from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.drivers import ChromeDriver
driver = ChromeDriver().get_chrome_driver()

class HeaderElements:
    # sign up button
    def sign_up_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "signin2")))
    # Username input
    def sign_up_user_name(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'sign-username')))

        return element
    # Password input
    def sign_up_password(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'sign-password')))

        return element
    # Sign up button
    def sign_up_inner_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="signInModal'
                                                                                           '"]/div/div/div[3]/button['
                                                                                           '2]')))
        return element
    # Sign up close button
    def sign_up_close_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]")))

        return element
    # Home button
    def home_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[1]/a")))

        return element
    # Contact button
    def contact_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[2]/a")))

        return element
    # About us button

    def about_us_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[3]/a")))

        return element
    # Cart button
    def cart_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "cartur")))

        return element
    # cart place order button
    def cart_place_order_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div[2]/button")))

        return element
    # login button
    def login_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "login2")))

        return element
    # login username input
    def login_username(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "loginusername")))

        return element
    # login password input
    def login_password(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "loginpassword")))

        return element
    # login  log in button
    def login_log_in_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")))

        return element
    # login close button
    def login_close_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]")))

        return element

    # Logo matches

    def logo_left_top(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/a/img")))

        return element

    # Welcome <User> top right

    def welcome_user(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "nameofuser")))

        return element

    # Log out button

    def logout_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "logout2")))

        return element

