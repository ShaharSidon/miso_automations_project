import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.drivers import ChromeDriver

class TestEndtoendPurchase(unittest.TestCase):
    # setting up driver
    def setUp(self):
        try:
            chromedriver_path = "./utils/chromedriver.exe"
            self.service = Service(executable_path=chromedriver_path)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            driver = ChromeDriver()
            self.chrome_driver = driver.get_chrome_driver()
        except AssertionError:
            self.chrome_driver.quit()

    def tearDown(self):
        # quit when done
        self.chrome_driver.quit()

    def test_e2e_purchase(self):
        # open browser with domain
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get('https://demoblaze.com/index.html')
        # enter item in homepage
        item = self.chrome_driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
        item.click()
        # add item to cart
        add = self.chrome_driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a')
        add.click()
        # move to cart page
        cart = self.chrome_driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a')
        cart.click()
        # place order in the cart page
        place_order = self.chrome_driver.find_element(By.XPATH, '/html/body/div[6]/div/div[2]/button')
        place_order.click()
        self.chrome_driver.switch_to.accept()
        # enter valid credantial to order form (only name and credit card required)
        name = self.chrome_driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[1]/input')
        name.send_keys('yoel')
        credit_card = self.chrome_driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[4]/input')
        credit_card.send_keys('1231-123-1234')
        # purchase order
        purchase_button = self.chrome_driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')
        purchase_button.click()
        assert self.chrome_driver.current_url == 'https://demoblaze.com/cart.html'




