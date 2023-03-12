import time

from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from utils.drivers import ChromeDriver


class PurchasingSingleItemAndMultipleItems(unittest.TestCase):
    # TS53 verify that a user can purchase an item

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("All tests completed")

    def test_1_purcahse_single_item(self):
        # locating the 'Phones' category, add an item to the cart and purchase
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)
        time.sleep(5)

        cart = self.driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[4]/a")
        cart.click()

        place_order = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button")
        place_order.click()

        purchase = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
        purchase.click()

    # TS54 verify that a user can purchase multiple items

    def test_2_purchasing_multiple_items(self):
        # navigating to the site, clicking the 'Phones' category, adding multiple items to the cart purchasing.
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)
        time.sleep(5)

        home_page = self.driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[1]/a")
        home_page.click()

        phone2 = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a")
        phone2.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)
        time.sleep(5)

        cart = self.driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[4]/a")
        cart.click()

        place_order = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button")
        place_order.click()

        purchase = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
        purchase.click()
