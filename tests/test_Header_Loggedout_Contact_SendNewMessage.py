import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.drivers import ChromeDriver

class TestContact (unittest.TestCase):
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

    def test_contact_button(self):
        # open browser with domain
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get('https://demoblaze.com/index.html')
        # click about us button
        contact = self.chrome_driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[3]/a')
        contact.click()
        # enter email
        email = self.chrome_driver.find_element(By.ID, 'recipient-email')
        email.send_keys('jerry23@gmail.com')
        # enter message
        message = self.chrome_driver.find_element(By.ID, 'message-text')
        message.send_keys('blalbalbalbla')
        # click send new message button click
        send_message = self.chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/button[2]')
        send_message.click()
        assert self.chrome_driver.current_url == 'https://demoblaze.com/cart.html'