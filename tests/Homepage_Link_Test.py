import time

from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from utils.drivers import ChromeDriver


class DisplyingThePhonesPage(unittest.TestCase):
    # TS58- Displaying the phones page

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 1 completed")

    def test_1_displying_phones_page(self):
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[2]")
        phones_cat.click()
        time.sleep(5)


class DisplayingLaptops(unittest.TestCase):
    # TS59 Displying Laptops

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 2  completed")

    def test_2_displying_laptops(self):
        self.driver.get("https://www.demoblaze.com/")
        laptops_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
        laptops_cat.click()
        time.sleep(5)


class DisplayMonitorsPage(unittest.TestCase):
    # TS60- display monitors page

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 3  completed")

    def test_3_display_monitors(self):
        self.driver.get("https://www.demoblaze.com/")
        monitors_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[4]")
        monitors_cat.click()
        time.sleep(5)

