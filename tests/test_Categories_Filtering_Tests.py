# importing the necessary libraries
import unittest
from utils.drivers import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# creating the class for the tests
class TestingFilteringByCategories(unittest.TestCase):
    # creating the setup for the tests
    def setUp(self):
        # attempt to do the following actions
        try:
            self.driver = ChromeDriver().get_chrome_driver()
            self.driver.implicitly_wait(5)
            self.driver.get("https://www.demoblaze.com/index.html")
            self.driver.maximize_window()
        # if you discovered a AssertionError do this
        except AssertionError:
            self.driver.quit()

    # creating the teardown for the tests
    def tearDown(self):
        self.driver.quit()

    # the start of the first test:
    def test_1_filter_by_phones(self):
        # find the filter button for phones and press it
        button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                     '/html/body/div[5]/div/div['
                                                                                     '1]/div/a[2]')))
        button.click()
        # wait for the page to update and make sure that a change happened
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html#"
        # get the name of a product and check that the name displayed is the name that should be there
        # according to the filter
        phone = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                    '/html/body/div[5]/div/'
                                                                                    'div[2]/div/div[1]/div/'
                                                                                    'div/h4'))) \
            .get_attribute("innerText")
        assert phone == "Samsung galaxy s6"

    # the start of the second test:
    def test_2_filter_by_laptops(self):
        # find the filter button for phones and press it
        button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                     '/html/body/div[5]/div/div['
                                                                                     '1]/div/a[3]')))
        button.click()
        # wait for the page to update and make sure that a change happened
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html#"
        # get the name of a product and check that the name displayed is the name that should be there
        # according to the filter
        laptop = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                     '/html/body/div[5]/div/'
                                                                                     'div[2]/div/div[1]/div/'
                                                                                     'div/h4'))) \
            .get_attribute("innerText")
        assert laptop == "Sony vaio i5"

    # the start of the second test:
    def test_3_filter_by_monitors(self):
        # find the filter button for phones and press it
        button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                     '/html/body/div[5]/div/div['
                                                                                     '1]/div/a[4]')))
        button.click()
        # wait for the page to update and make sure that a change happened
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html#"
        # get the name of a product and check that the name displayed is the name that should be there
        # according to the filter
        monitor = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '/html/body/div[5]/div/'
                                                                                      'div[2]/div/div[1]/div/'
                                                                                      'div/h4'))) \
            .get_attribute("innerText")
        assert monitor == "Apple monitor 24"
