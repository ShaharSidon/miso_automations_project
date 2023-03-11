# importing the necessary libraries
import unittest
from utils.drivers import get_chrome_driver
from utils.Header_Locators import HeaderElements
from selenium.webdriver.support import expected_conditions as EC


# creating the class for the tests
class UITextTesting(unittest.TestCase):
    # creating the setup for the tests
    def setUp(self) -> None:
        self.driver = get_chrome_driver()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        self.locator = HeaderElements(self.driver)

    # creating the teardown for the tests
    def tearDown(self) -> None:
        self.driver.quit()

    # the start of the first test:
    def test_1_Home_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.pressing_home_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Home (current)"

    # the start of the second test:
    def test_2_Contact_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.pressing_contact_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Contact"

    # the start of the third test:
    def test_3_About_us_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.pressing_about_us_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "About us"

    # the start of the fourth test:
    def test_4_Cart_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.pressing_cart_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Cart"

    # the start of the fifth test:
    def test_5_Log_in_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.pressing_login_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Log in"

    # the start of the sixth test:
    def test_6_Sign_up_button_text(self):
        # finding the button and extracting the text from it
        text = self.locator.pressing_sign_up_button()
        test_text = text.get_attribute("text")
        # asserting that the correct text was displayed
        assert test_text == "Sign up"

    # the start of the seventh test:
    def test_7_store_logo_existence_and_correct_picture(self):
        # finding the logo in the header
        logo = self.locator.find_logo_left_top_bar()
        # asserting that the logo is visible to the users
        self.assertTrue(EC.presence_of_element_located(logo))
        # getting the url of the logo and asserting that it is the correct url
        picture = logo.get_attribute("src")
        assert picture == "https://www.demoblaze.com/bm.png"

    # the start of the eighth test:
    def test_8_store_name_text(self):
        # finding the store name and extracting the text from it
        text = self.locator.find_store_name_left_top_bar()
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == " PRODUCT STORE"
