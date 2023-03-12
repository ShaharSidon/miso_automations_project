# importing the necessary libraries
import unittest
from utils.drivers import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# creating the class for the tests
class SendingAMessageTest(unittest.TestCase):
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
    def test_1_send_a_valid_message(self):
        # opening the contact window
        first_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav"
                                                                                                     "/div[1]/ul/li["
                                                                                                     "2]/a")))
        first_button.click()
        # inputting a valid email into the email textbox
        email_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-email")))
        email_textbox.send_keys("Khoth@gmail.com")
        # inputting a valid name into the name textbox
        name_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-name")))
        name_textbox.send_keys("Khoth Voor")
        # inputting a valid message into the message textbox
        message_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "message-text")))
        message_textbox.send_keys("Commander Khoth Voor has a heavy weight on his shoulders. He is the son of the "
                                  "Leader of the Illuminen Alliance and the protection of the known universe from the "
                                  "dreaded Swarm is his responsibility.")
        # pressing the button and sending the message
        second_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                            "1]/div/div/div[3]/button["
                                                                                            "2]")))
        second_button.click()
        # asserting that we got the right message
        assert self.driver.switch_to.alert.text == "Thanks for the message!!"

    # the start of the second test:
    def test_2_send_an_invalid_message_email(self):
        # opening the contact window
        first_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav"
                                                                                                     "/div[1]/ul/li["
                                                                                                     "2]/a")))
        first_button.click()
        # inputting an invalid email into the email textbox
        email_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-email")))
        email_textbox.send_keys("Khoth")
        # inputting a valid name into the name textbox
        name_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-name")))
        name_textbox.send_keys("Khoth Voor")
        # inputting a valid message into the message textbox
        message_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "message-text")))
        message_textbox.send_keys("Commander Khoth Voor has a heavy weight on his shoulders. He is the son of the "
                                  "Leader of the Illuminen Alliance and the protection of the known universe from the "
                                  "dreaded Swarm is his responsibility.")
        # pressing the button and sending the message
        second_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                                      "1]/div/div"
                                                                                                      "/div[3]/button["
                                                                                                      "2]")))
        second_button.click()
        # asserting that we got the right message
        assert self.driver.switch_to.alert.text != "Thanks for the message!!"

    # the start of the third test:
    def test_3_send_an_invalid_message_name(self):
        # opening the contact window
        first_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav"
                                                                                                     "/div[1]/ul/li["
                                                                                                     "2]/a")))
        first_button.click()
        # inputting a valid email into the email textbox
        email_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-email")))
        email_textbox.send_keys("Khoth@gmail.com")
        # inputting an invalid name into the name textbox
        name_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-name")))
        name_textbox.send_keys("Khoth Voor"*10)
        # inputting a valid message into the message textbox
        message_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "message-text")))
        message_textbox.send_keys("Commander Khoth Voor has a heavy weight on his shoulders. He is the son of the "
                                  "Leader of the Illuminen Alliance and the protection of the known universe from the "
                                  "dreaded Swarm is his responsibility.")
        # pressing the button and sending the message
        second_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                                      "1]/div/div"
                                                                                                      "/div[3]/button["
                                                                                                      "2]")))
        second_button.click()
        # asserting that we got the right message
        assert self.driver.switch_to.alert.text != "Thanks for the message!!"

    # the start of the fourth test:
    def test_4_send_an_invalid_message_actual_message_text(self):
        # opening the contact window
        first_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav"
                                                                                                     "/div[1]/ul/li["
                                                                                                     "2]/a")))
        first_button.click()
        # inputting a valid email into the email textbox
        email_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-email")))
        email_textbox.send_keys("Khoth@gmail.com")
        # inputting a valid name into the name textbox
        name_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-name")))
        name_textbox.send_keys("Khoth Voor")
        # inputting an invalid message into the message textbox
        message_textbox = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "message-text")))
        message_textbox.send_keys("Commander Khoth Voor has a heavy weight on his shoulders. He is the son of the "
                                  "Leader of the Illuminen Alliance and the protection of the known universe from the "
                                  "dreaded Swarm is his responsibility."*3)
        # pressing the button and sending the message
        second_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                                      "1]/div/div"
                                                                                                      "/div[3]/button["
                                                                                                      "2]")))
        second_button.click()
        # asserting that we got the right message
        assert self.driver.switch_to.alert.text != "Thanks for the message!!"
