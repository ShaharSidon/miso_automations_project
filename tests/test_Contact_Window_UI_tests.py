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
    def test_1_new_message_title_text(self):
        # opening the contact window
        contact_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body"
                                                                                                       "/nav/div["
                                                                                                       "1]/ul/li["
                                                                                                       "2]/a")))
        contact_button.click()
        # finding the title and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, "exampleModalLabel")))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "New message"

    # the start of the second test:
    def test_2_contact_email_title_text(self):
        # opening the contact window
        contact_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body"
                                                                                                       "/nav/div["
                                                                                                       "1]/ul/li["
                                                                                                       "2]/a")))
        contact_button.click()
        # finding the title and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                   "1]/div/div/div["
                                                                                   "2]/form/div[1]/label")))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Contact Email:"

    # the start of the third test:
    def test_3_name_title_text(self):
        # opening the contact window
        contact_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body"
                                                                                                       "/nav/div["
                                                                                                       "1]/ul/li["
                                                                                                       "2]/a")))
        contact_button.click()
        # finding the title and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*['
                                                                                   '@id="exampleModal'
                                                                                   '"]/div/div/div['
                                                                                   '2]/form/div['
                                                                                   '2]/label')))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Contact Name:"

    # the start of the fourth test:
    def test_4_message_title_text(self):
        # opening the contact window
        contact_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body"
                                                                                                       "/nav/div["
                                                                                                       "1]/ul/li["
                                                                                                       "2]/a")))
        contact_button.click()
        # finding the title and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                   "1]/div/div/div["
                                                                                   "2]/form/div[3]/label")))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Message:"

    # the start of the fifth test:
    def test_5_close_button_text(self):
        # opening the contact window
        contact_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body"
                                                                                                       "/nav/div["
                                                                                                       "1]/ul/li["
                                                                                                       "2]/a")))
        contact_button.click()
        # finding the button and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                   "1]/div/div/div[3]/button["
                                                                                   "1]")))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Close"

    # the start of the sixth test:
    def test_6_send_message_button_text(self):
        # opening the contact window
        contact_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body"
                                                                                                       "/nav/div["
                                                                                                       "1]/ul/li["
                                                                                                       "2]/a")))
        contact_button.click()
        # finding the button and extracting the text from it
        text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                   "1]/div/div/div[3]/button["
                                                                                   "2]")))
        test_text = text.get_attribute("innerText")
        # asserting that the correct text was displayed
        assert test_text == "Send message"
