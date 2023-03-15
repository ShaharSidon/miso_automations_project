# importing the necessary libraries
import unittest
from src.utils.drivers import ChromeDriver
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
    def test_1_store_logo_existence_and_correct_picture(self):
        # finding the logo in the header
        logo = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   '#fotcont > div:nth-child(3) > '
                                                                                   'div >'
                                                                                   'div > h4 > img')))
        # asserting that the logo is visible to the users
        self.assertTrue(EC.presence_of_element_located(logo))
        # getting the url of the logo and asserting that it is the correct url
        picture = logo.get_attribute("src")
        assert picture == "https://www.demoblaze.com/bm.png"

    # the start of the second test:
    def test_2_store_name_text(self):
        # finding the store name and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   '#fotcont > div:nth-child(3) > '
                                                                                   'div >'
                                                                                   'div > h4')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == " PRODUCT STORE"

    # the start of the third test:
    def test_3_About_us_title_text(self):
        # finding the title and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   '#fotcont > div:nth-child(1) > '
                                                                                   'div > div > h4')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "About Us"

    # the start of the fourth test:
    def test_4_About_us_description_text(self):
        # finding the description and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   '#fotcont > div:nth-child(1) > '
                                                                                   'div >'
                                                                                   'div > p')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "We believe performance needs to be validated at every stage of the software development " \
                            "cycle and our open source compatible, massively scalable platform makes that a reality."

    # the start of the fifth test:
    def test_5_Get_in_Touch_title_text(self):
        # finding the title and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   '#fotcont > div.col-sm-3.col-lg'
                                                                                   '-3.col'
                                                                                   '-md-3 > div > div > h4 > b')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Get in Touch"

    # the start of the sixth test:
    def test_6_Address_text(self):
        # finding the description and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   '#fotcont > div.col-sm-3.col-lg'
                                                                                   '-3.col'
                                                                                   '-md-3 > div > div > '
                                                                                   'p:nth-child(2)')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Address: 2390 El Camino Real"

    # the start of the seventh test:
    def test_7_Phone_text(self):
        # finding the description and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   '#fotcont > div.col-sm-3.col-lg'
                                                                                   '-3.col'
                                                                                   '-md-3 > div > div > '
                                                                                   'p:nth-child(3)')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Phone: +440 123456"

    # the start of the eighth test:
    def test_8_Email_text(self):
        # finding the description and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   '#fotcont > div.col-sm-3.col-lg'
                                                                                   '-3.col'
                                                                                   '-md-3 > div > div > '
                                                                                   'p:nth-child(4)')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Email: demo@blazemeter.com"

    # the start of the ninth test:
    def test_9_Copyright_text(self):
        # finding the description and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                   'body > footer > p')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Copyright © Product Store 2017"
