from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.Locators.Contact import ContactLocators

contact = ContactLocators()


class ContactPage:

    def __init__(self, driver):
        self.driver = driver

    def find_email_title(self):
        email_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.contact_email_title)))

    def find_new_message_title(self):
        new_message_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.new_message_title)))

    def find_message_title(self):
        message_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.message_title)))

    def find_contact_name_title(self):
        name_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.contact_name_title)))

    def set_contact_email(self):
        contact_email = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.contact_email_field_id)))
        contact_email.send_keys()

    def set_contact_name(self):
        contact_name = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.contact_name_field_id)))
        contact_name.send_keys()

    def set_message(self):
        contact_email_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.message_field_id)))
        contact_email_title.send_keys()

    def set_x_button(self):
        x_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.x_button_xpath)))
        x_btn.click()

    def set_send_message(self):
        send_message = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.send_message_xpath)))
        send_message.click()

    def set_close_button(self):
        close_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, contact.close_xpath)
                                             ))
        close_btn.click()
