import time

from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from utils.drivers import ChromeDriver


class LogoButton(unittest.TestCase):
    # TS57- Clicking on the logo button and verifying that the homepage is displayed

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 1 completed")

    def test_1_click_on_logo(self):
        self.driver.get("https://www.demoblaze.com/")
        cart = self.driver.find_element(By.CSS_SELECTOR, "#navbarExample > ul > li:nth-child(4) > a")
        cart.click()
        time.sleep(5)
        logo = self.driver.find_element(By.ID, "nava")
        logo.click()
        time.sleep(5)

