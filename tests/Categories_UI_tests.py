# importing the necessary libraries
import unittest
from utils.drivers import get_chrome_driver
from utils.Homepage_Locator import HomepageElements


# creating the class for the tests
class UITextTesting(unittest.TestCase):
    # creating the setup for the tests
    def setUp(self) -> None:
        self.driver = get_chrome_driver()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        self.locator = HomepageElements(self.driver)

    # creating the teardown for the tests
    def tearDown(self) -> None:
        self.driver.quit()

    # the start of the first test:
    def test_1_categories_title_text(self):
        # finding the title and extracting the text from it
        text = self.locator.find_category_text()
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "CATEGORIES"

    # the start of the second test:
    def test_2_Phones_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.find_category_phones_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Phones"

    # the start of the third test:
    def test_3_Laptops_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.find_category_laptops_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Laptops"

    # the start of the fourth test:
    def test_4_Monitors_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.find_category_monitors_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Monitors"
