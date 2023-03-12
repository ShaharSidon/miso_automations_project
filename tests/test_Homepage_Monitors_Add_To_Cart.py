from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from utils.drivers import ChromeDriver
import time


class AddingAppleMonitor24ToCart(unittest.TestCase):
    # Test Scenario 48: Adding Apple Monitor 24 to cart

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 1 completed")

    def test_1_add_apple_monitor_24_to_cart(self):
        # Go to the website
        self.driver.get("https://www.demoblaze.com/")

        # Click on the monitors category
        monitors_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[4]")
        monitors_cat.click()
        time.sleep(5)

        # Click on the Apple Monitor 24 product
        laptop = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")
        laptop.click()
        time.sleep(5)

        # Click on the "Add to cart" button
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()

        # Wait for 2 seconds to ensure the item is added to the cart
        WebDriverWait(self.driver, 2)


class AddingAsusFullHdToCart(unittest.TestCase):
    # Test Scenario 49: Adding Asus full HD to cart

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 2 completed")

    def test_2_add_asus_full_hd_to_cart(self):
        # Go to the website
        self.driver.get("https://www.demoblaze.com/")

        # Click on the monitors category
        monitors_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[4]")
        monitors_cat.click()
        time.sleep(5)

        # Click on the Asus Full HD product
        laptop = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a")
        laptop.click()
        time.sleep(5)

        # Click on the "Add to cart" button
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()

        # Wait for 2 seconds to ensure the item is added to the cart
        WebDriverWait(self.driver, 2)
