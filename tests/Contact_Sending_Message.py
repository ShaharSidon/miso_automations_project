# importing the necessary libraries
import unittest
from utils.drivers import get_chrome_driver
from utils.Header_Locators import HeaderElements


# creating the class for the tests
class SendingAMessageTest(unittest.TestCase):
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
    def test_1_send_a_valid_message(self):
        # opening the contact window
        first_button = self.locator.pressing_contact_button()
        first_button.click()
        # inputting a valid email into the email textbox
        email_textbox = self.locator.insert_contact_email_input()
        email_textbox.send_keys("Khoth@gmail.com")
        # inputting a valid name into the name textbox
        name_textbox = self.locator.insert_contact_name_input()
        name_textbox.send_keys("Khoth Voor")
        # inputting a valid message into the message textbox
        message_textbox = self.locator.insert_contact_message()
        message_textbox.send_keys("Commander Khoth Voor has a heavy weight on his shoulders. He is the son of the "
                                  "Leader of the Illuminen Alliance and the protection of the known universe from the "
                                  "dreaded Swarm is his responsibility.")
        # pressing the button and sending the message
        second_button = self.locator.pressing_send_contact_message()
        second_button.click()
        # asserting that we got the right message
        assert self.driver.switch_to.alert.text == "Thanks for the message!!"

    # the start of the second test:
    def test_2_send_an_invalid_message_email(self):
        # opening the contact window
        first_button = self.locator.pressing_contact_button()
        first_button.click()
        # inputting an invalid email into the email textbox
        email_textbox = self.locator.insert_contact_email_input()
        email_textbox.send_keys("Khoth")
        # inputting a valid name into the name textbox
        name_textbox = self.locator.insert_contact_name_input()
        name_textbox.send_keys("Khoth Voor")
        # inputting a valid message into the message textbox
        message_textbox = self.locator.insert_contact_message()
        message_textbox.send_keys("Commander Khoth Voor has a heavy weight on his shoulders. He is the son of the "
                                  "Leader of the Illuminen Alliance and the protection of the known universe from the "
                                  "dreaded Swarm is his responsibility.")
        # pressing the button and sending the message
        second_button = self.locator.pressing_send_contact_message()
        second_button.click()
        # asserting that we got the right message
        assert self.driver.switch_to.alert.text != "Thanks for the message!!"

    # the start of the third test:
    def test_3_send_an_invalid_message_name(self):
        # opening the contact window
        first_button = self.locator.pressing_contact_button()
        first_button.click()
        # inputting a valid email into the email textbox
        email_textbox = self.locator.insert_contact_email_input()
        email_textbox.send_keys("Khoth@gmail.com")
        # inputting an invalid name into the name textbox
        name_textbox = self.locator.insert_contact_name_input()
        name_textbox.send_keys("Khoth Voor"*10)
        # inputting a valid message into the message textbox
        message_textbox = self.locator.insert_contact_message()
        message_textbox.send_keys("Commander Khoth Voor has a heavy weight on his shoulders. He is the son of the "
                                  "Leader of the Illuminen Alliance and the protection of the known universe from the "
                                  "dreaded Swarm is his responsibility.")
        # pressing the button and sending the message
        second_button = self.locator.pressing_send_contact_message()
        second_button.click()
        # asserting that we got the right message
        assert self.driver.switch_to.alert.text != "Thanks for the message!!"

    # the start of the fourth test:
    def test_4_send_an_invalid_message_actual_message_text(self):
        # opening the contact window
        first_button = self.locator.pressing_contact_button()
        first_button.click()
        # inputting a valid email into the email textbox
        email_textbox = self.locator.insert_contact_email_input()
        email_textbox.send_keys("Khoth@gmail.com")
        # inputting a valid name into the name textbox
        name_textbox = self.locator.insert_contact_name_input()
        name_textbox.send_keys("Khoth Voor")
        # inputting an invalid message into the message textbox
        message_textbox = self.locator.insert_contact_message()
        message_textbox.send_keys("Commander Khoth Voor has a heavy weight on his shoulders. He is the son of the "
                                  "Leader of the Illuminen Alliance and the protection of the known universe from the "
                                  "dreaded Swarm is his responsibility."*3)
        # pressing the button and sending the message
        second_button = self.locator.pressing_send_contact_message()
        second_button.click()
        # asserting that we got the right message
        assert self.driver.switch_to.alert.text != "Thanks for the message!!"
