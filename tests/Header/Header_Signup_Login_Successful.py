import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.drivers import ChromeDriver

class TestSignupLoginSuccessful(unittest.TestCase):
    # setting up driver
    def setUp(self):
        try:
            chromedriver_path = "./utils/chromedriver.exe"
            self.service = Service(executable_path=chromedriver_path)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            driver = ChromeDriver()
            self.chrome_driver = driver.get_chrome_driver()
        except AssertionError:
            self.chrome_driver.quit()

    def tearDown(self):
        # quit when done
        self.chrome_driver.quit()

    def test_1_signup_successful(self):
        # open browser with domain
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get('https://demoblaze.com/index.html')
        # signing up with once to determine successful sign up (username, password)
        signup_button = self.chrome_driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[8]/a')
        signup_button.click()
        username = self.chrome_driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[1]/input')
        username.send_keys('mrtony1234')
        password = self.chrome_driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/form/div[2]/input')
        password.send_keys('shhhh1234')
        signup_accept = self.chrome_driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/button[2]')
        signup_accept.click()
        assert self.chrome_driver.current_url == 'https://demoblaze.com/index.html'

    def test_2_login_successful(self):
        # open browser with domain
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get('https://demoblaze.com/index.html')
        # login with once to determine successful login (username, password)
        login_button = self.chrome_driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[5]/a')
        login_button.click()
        username = self.chrome_driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input')
        username.send_keys('mrtony1234')
        password = self.chrome_driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[2]/input')
        password.send_keys('shhhh1234')
        login_accept = self.chrome_driver.find_element(By.XPATH,
                                                       '/html/body/div[3]/div/div/div[2]/form/div[2]/input')
        login_accept.click()
        assert self.chrome_driver.current_url == 'https://demoblaze.com/index.html'