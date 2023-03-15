import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from src.utils.drivers import ChromeDriver
from selenium.webdriver.common.by import By


class TestImageleftArrowShift(unittest.TestCase):

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

    def test_image_left_arrow_shift(self):
        # open browser with domain
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get('https://demoblaze.com/index.html')
        # click the left arrow
        left_arrow = self.chrome_driver.find_element(By.XPATH, '/html/body/nav/div[2]/div/a[1]/span[1]')
        left_arrow.click()
        assert self.chrome_driver.current_url == 'https://demoblaze.com/index.html'