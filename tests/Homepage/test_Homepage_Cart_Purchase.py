import time
from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from src.utils.drivers import ChromeDriver
from selenium.webdriver.support import expected_conditions as EC


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
        first_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                           '/html/body/div[5]/div/'
                                                                                           'div[2]/div/div[1]/div/'
                                                                                           'div/h4')))
        first_button.click()
        second_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '/html/body/div['
                                                                                            '5]/div/div[2]/div['
                                                                                            '2]/div/a')))
        second_button.click()
        third_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cartur"
                                                                                            )))
        third_button.click()

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
        first_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                           '/html/body/div[5]/div/'
                                                                                           'div[2]/div/div[1]/div/'
                                                                                           'div/h4')))
        first_button.click()
        second_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '/html/body/div['
                                                                                            '5]/div/div[2]/div['
                                                                                            '2]/div/a')))
        second_button.click()
        third_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cartur"
                                                                                            )))
        third_button.click()
        WebDriverWait(self.driver, 2)
        time.sleep(5)

        home_page = self.driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[1]/a")
        home_page.click()

        first_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                           '/html/body/div[5]/div/'
                                                                                           'div[2]/div/div[1]/div/'
                                                                                           'div/h4')))
        first_button.click()
        second_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '/html/body/div['
                                                                                            '5]/div/div[2]/div['
                                                                                            '2]/div/a')))
        second_button.click()
        third_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cartur"
                                                                                            )))
        third_button.click()
        WebDriverWait(self.driver, 2)
        time.sleep(5)

        cart = self.driver.find_element(By.XPATH, "/html/body/nav/div/div/ul/li[4]/a")
        cart.click()

        place_order = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button")
        place_order.click()

        purchase = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")
        purchase.click()
