# importing the necessary libraries
import unittest
from utils.drivers import get_chrome_driver
from utils.Header_Locators import HeaderElements


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
    def test_1_new_message_title_text(self):
        # opening the contact window
        contact_button = self.locator.pressing_contact_button()
        contact_button.click()
        # finding the title and extracting the text from it
        text = self.locator.find_new_message_title()
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "New message"

    # the start of the second test:
    def test_2_contact_email_title_text(self):
        # opening the contact window
        contact_button = self.locator.pressing_contact_button()
        contact_button.click()
        # finding the title and extracting the text from it
        text = self.locator.find_contact_email_title()
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Contact Email:"

    # the start of the third test:
    def test_3_name_title_text(self):
        # opening the contact window
        contact_button = self.locator.pressing_contact_button()
        contact_button.click()
        # finding the title and extracting the text from it
        text = self.locator.find_contact_name_title()
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Contact Name:"

    # the start of the fourth test:
    def test_4_message_title_text(self):
        # opening the contact window
        contact_button = self.locator.pressing_contact_button()
        contact_button.click()
        # finding the title and extracting the text from it
        text = self.locator.find_message_title()
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Message:"

    # the start of the fifth test:
    def test_5_close_button_text(self):
        # opening the contact window
        contact_button = self.locator.pressing_contact_button()
        contact_button.click()
        # finding the button and extracting the text from it
        text = self.locator.pressing_the_close_button_contact()
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Close"

    # the start of the sixth test:
    def test_6_send_message_button_text(self):
        # opening the contact window
        contact_button = self.locator.pressing_contact_button()
        contact_button.click()
        # finding the button and extracting the text from it
        text = self.locator.pressing_send_contact_message()
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Send message"
