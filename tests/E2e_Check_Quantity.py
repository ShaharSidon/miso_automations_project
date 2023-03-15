import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.drivers import ChromeDriver

class TestQuantityChange(unittest.TestCase):
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

    def test_quantity_change(self):
        # open browser with domain
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get('https://demoblaze.com/index.html')
        # enter item in homepage
        item = self.chrome_driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')
        item.click()
        # add two samsung galaxy s6 to cart
        add = self.chrome_driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a')
        add.click()
        self.chrome_driver.switch_to.accept()
        add = self.chrome_driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div[2]/div/a')
        add.click()
        self.chrome_driver.switch_to.accept()
        # move to cart page
        cart = self.chrome_driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[4]/a')
        cart.click()
        # count the quantity of samsung galaxy
        count_item = self.chrome_driver.find_element(By.XPATH, '/html/body/div[6]/div/div[1]/div/table/tbody/tr[1]/td[2]').count()
        # to assume that galaxy s6 cost 360$ so two items are 720$, now validating the items cost 720$
        assert count_item == 2, f"quantity isnt working right"




