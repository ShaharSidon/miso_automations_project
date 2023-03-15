import time

# from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from src.utils.drivers import ChromeDriver


class LogoButton(unittest.TestCase):
    # TS57- Clicking on the logo button and verifying that the homepage is displayed

    def setUp(self):
        # Initialize ChromeDriver and maximize window
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser window after test completion
        self.driver.quit()
        print("Test 1 completed")

    def test_1_click_on_logo(self):
        # Open the demo blaze website
        self.driver.get("https://www.demoblaze.com/")

        # Find the cart button and click on it
        cart = self.driver.find_element(By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(4) > a")
        cart.click()

        # Wait for 5 seconds
        time.sleep(5)

        # Find the logo button and click on it
        logo = self.driver.find_element(By.ID, "nava")
        logo.click()

        # Wait for 5 seconds
        time.sleep(5)
