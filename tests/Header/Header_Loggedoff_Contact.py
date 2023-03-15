import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.utils.drivers import ChromeDriver

class TestContactButton(unittest.TestCase):
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
        # click contact button
        contact = self.chrome_driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[2]/a')
        contact.click()
        contact_newmessage_popup = self.chrome_driver.find_element(By.ID, 'exampleModalLabel')
        self.assertTrue(contact_newmessage_popup.isDisplayed())