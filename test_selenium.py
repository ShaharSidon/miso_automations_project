import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.drivers import ChromeDriver


class TestOrangeHrmLoginPage(unittest.TestCase):
    def setUp(self):
        try:
            chromedriver_path = "src/utils/chromedriver.exe"
            self.service = Service(executable_path=chromedriver_path)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            # self.chrome_driver = webdriver.Chrome(options=chrome_options)
            driver = ChromeDriver()
            self.chrome_driver = driver.get_chrome_driver()
        except AssertionError:
            self.chrome_driver.quit()

    def tearDown(self):
        self.chrome_driver.quit()

    def test_1_valid_login(self):

        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

        valid_username = self.chrome_driver.find_element(By.NAME, 'username')
        valid_username.send_keys('Admin')
        valid_password = self.chrome_driver.find_element(By.NAME, 'password')
        valid_password.send_keys('admin123')
        login_button = self.chrome_driver.find_element(By.CSS_SELECTOR, '#app > div.orangehrm-login-layout > div > '
                                                                        'div.orangehrm-login-container > div > '
                                                                        'div.orangehrm-login-slot > '
                                                                        'div.orangehrm-login-form > form > '
                                                                        'div.oxd-form-actions.orangehrm-login-action > '
                                                                        'button')
        login_button.click()
        assert self.chrome_driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/' \
                                                 'index'


# Set up the Chrome driver and navigate to the login page
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Enter login credentials and submit the form
username_field = driver.find_element(By.ID, "txtUsername")
password_field = driver.find_element(By.ID, "txtPassword")
submit_button = driver.find_element(By.ID, "btnLogin")
username_field.send_keys("Admin")
password_field.send_keys("admin123")
submit_button.click()

# Wait for the dashboard to load and verify that the page title contains "Dashboard"
dashboard_title = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Dashboard')]")))
assert "Dashboard" in driver.title


# Close the browser window
driver.quit()

# poleg was here

