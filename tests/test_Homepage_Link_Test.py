import time

# from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from utils.drivers import ChromeDriver


class DisplyingThePhonesPage(unittest.TestCase):
    # This class is for testing the display of the phones category page

    def setUp(self):
        # Set up the ChromeDriver and maximize window
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser window after the test has completed
        self.driver.quit()
        print("Test 1 completed")

    def test_1_displying_phones_page(self):
        # Navigate to the demo website and click on the phones category link
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[2]")
        phones_cat.click()
        time.sleep(5)


class DisplayingLaptops(unittest.TestCase):
    # This class is for testing the display of the laptops category page

    def setUp(self):
        # Set up the ChromeDriver and maximize window
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser window after the test has completed
        self.driver.quit()
        print("Test 2  completed")

    def test_2_displying_laptops(self):
        # Navigate to the demo website and click on the laptops category link
        self.driver.get("https://www.demoblaze.com/")
        laptops_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
        laptops_cat.click()
        time.sleep(5)


class DisplayMonitorsPage(unittest.TestCase):
    # This class is for testing the display of the monitors category page

    def setUp(self):
        # Set up the ChromeDriver and maximize window
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser window after the test has completed
        self.driver.quit()
        print("Test 3  completed")

    def test_3_display_monitors(self):
        # Navigate to the demo website and click on the monitors category link
        self.driver.get("https://www.demoblaze.com/")
        monitors_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[4]")
        monitors_cat.click()
        time.sleep(5)
