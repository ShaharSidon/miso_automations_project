import unittest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from utils.drivers import ChromeDriver
from utils.Website_Link import Website_Link

# defining testcase class
class TestDemoBlazeWebsiteLink(unittest.TestCase):

    # setting up driver
    def setUp(self):
        try:
            chromedriver_path = "./utils/chromedriver.exe"
            self.service = Service(executable_path=chromedriver_path)
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--disable-extensions")
            self.chrome_driver = webdriver.Chrome(options=chrome_options)
            driver = ChromeDriver()
            self.chrome_driver = driver.get_chrome_driver()
        except AssertionError:
            self.chrome_driver.quit()

    # break after test
    def tearDown(self):
        self.chrome_driver.quit()

    # Get inside the website domain test
    def test_1_valid_get_to_website(self):
        self.website = Website_Link()
        self.domain = self.website.Web_link()
        self.chrome_driver.implicitly_wait(5)
        self.chrome_driver.maximize_window()
        self.chrome_driver.get(self.domain)
        assert self.chrome_driver.current_url == self.domain
