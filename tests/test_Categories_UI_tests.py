# importing the necessary libraries
import unittest
from utils.drivers import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# creating the class for the tests
class UITextTesting(unittest.TestCase):
    # creating the setup for the tests
    def setUp(self) -> None:
        self.driver = ChromeDriver().get_chrome_driver()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()

    # creating the teardown for the tests
    def tearDown(self) -> None:
        self.driver.quit()

    # the start of the first test:
    def test_1_categories_title_text(self):
        # finding the title and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                   '/html/body/div[5]/div/div['
                                                                                   '1]/div/a[1]')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "CATEGORIES"

    # the start of the second test:
    def test_2_Phones_button_text(self):
        # finding the button and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                   '/html/body/div[5]/div/div['
                                                                                   '1]/div/a[2]')))
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Phones"

    # the start of the third test:
    def test_3_Laptops_button_text(self):
        # finding the button and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                   '/html/body/div[5]/div/div['
                                                                                   '1]/div/a[3]')))
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Laptops"

    # the start of the fourth test:
    def test_4_Monitors_button_text(self):
        # finding the button and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                   '/html/body/div[5]/div/div['
                                                                                   '1]/div/a[4]')))
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Monitors"
