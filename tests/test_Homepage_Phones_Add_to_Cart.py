from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from utils.drivers import ChromeDriver


class AddingPhonesToCart(unittest.TestCase):
    # TS32- Adding Sumsung s6 to cart

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("All tests completed")

    def test_1_add_sumsungs6_to_cart(self):
        # clicking the 'Phones' category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(1) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)

    # TS33- Adding Nokia Lumia 1520 to cart

    def test_2_add_nokia_to_cart(self):
        # clicking the 'Phones' category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(2) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)

    # TS34- Adding Nexus 6 to cart

    def test_3_add_nexus_to_cart(self):
        # clicking the 'Phones' category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(3) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)

    # TS35- Adding Galaxy s7 to cart

    def test_4_add_sumsungs7_to_cart(self):
        # clicking the 'Phones' category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(4) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)

    # TS36- Adding Iphone 6 32g to cart

    def test_5_add_iphone_to_cart(self):
        # clicking the 'Phones' category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(5) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)

    # TS37- Adding SonyXperia to cart

    def test_6_add_sony_to_cart(self):
        # clicking the 'Phones' category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(5) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)

    # TS38- Adding HTC One M9 to cart

    def test_7_add_htc_to_cart(self):
        # clicking the 'Phones' category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        phones_cat = self.driver.find_element(By.CSS_SELECTOR, "#itemc")
        phones_cat.click()
        phone = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div:nth-child(7) > div > div > h4 > a")
        phone.click()

        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)
