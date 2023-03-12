from selenium.webdriver.support.ui import WebDriverWait
import unittest
from selenium.webdriver.common.by import By
from utils.drivers import ChromeDriver
import time


class AddingSonyVaioI5ToCart(unittest.TestCase):
    # TS39- Adding Sony Vaio i5 to cart

    def setUp(self):
        # setup function to initialize the webdriver and open the target webpage
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 1  completed")

    def test_1_add_sony_vaio_i5_to_cart(self):
        # locating the laptops category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        laptops_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
        laptops_cat.click()
        time.sleep(5)
        laptop = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")
        laptop.click()
        time.sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)


class AddingSonyVaioI7ToCart(unittest.TestCase):
    # TS40- Adding Sony Vaio i7 to cart

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 2  completed")

    def test_2_add_sony_vaio_i7_to_cart(self):
        # locating the laptops category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        laptops_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
        laptops_cat.click()
        time.sleep(5)
        laptop = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]/div/div/h4/a")
        laptop.click()
        time.sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)


class AddingMacBookAirToCart(unittest.TestCase):
    # TS41- Adding MacBook Air to cart

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 3  completed")

    def test_3_add_mac_book_air_to_cart(self):
        # locating the laptops category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        laptops_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
        laptops_cat.click()
        time.sleep(5)
        laptop = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[3]/div/div/h4/a")
        laptop.click()
        time.sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)


class AddingDellI78GbToCart(unittest.TestCase):
    # TS42- Adding Dell i7 8gb to cart

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 4  completed")

    def test_4_add_dell_i7_8gb_to_cart(self):
        # locating the laptops category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        laptops_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
        laptops_cat.click()
        time.sleep(5)
        laptop = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[4]/div/div/h4/a")
        laptop.click()
        time.sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)


class Adding2017DellToCart(unittest.TestCase):
    # TS43- Adding 2017 Dell 15.6 Inch to cart

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 5  completed")

    def test_5_add_dell_15_6_inch_to_cart(self):
        # locating the laptops category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        laptops_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
        laptops_cat.click()
        time.sleep(5)
        laptop = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[5]/div/div/h4/a")
        laptop.click()
        time.sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)


class AddingMacBookProToCart(unittest.TestCase):
    # TS44- Adding MacBookPro to cart

    def setUp(self):
        tempdriver = ChromeDriver()
        self.driver = tempdriver.get_chrome_driver()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        print("Test 6  completed")

    def test_6_add_mac_book_pro_to_cart(self):
        # locating the laptops category and adding the desired item to the cart
        self.driver.get("https://www.demoblaze.com/")
        laptops_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]")
        laptops_cat.click()
        time.sleep(5)
        laptop = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[6]/div/div/h4/a")
        laptop.click()
        time.sleep(5)
        add_to_cart = self.driver.find_element(By.CSS_SELECTOR, "#tbodyid > div.row > div > a")
        add_to_cart.click()
        WebDriverWait(self.driver, 2)




