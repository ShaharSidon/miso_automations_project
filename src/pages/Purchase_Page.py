# importing the necessary libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.Locators.Place_Order import PlaceOrderLocators


# creating the class for all the page specific actions in the purchase page
class PurchasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = PlaceOrderLocators()

    # sending a valid name into the name text box
    def send_valid_username(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.name_field_id)))
        username.send_keys("Khoth Voor")

    # sending a valid country into the country text box
    def send_valid_country(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.country_field_id)))
        username.send_keys("Arizona, USA")

    # sending a valid city into the city text box
    def send_valid_city(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.city_field_id)))
        username.send_keys("Sunrise")

    # sending a valid credit card number into the credit card text box
    def send_valid_credit_card_number(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.credit_card_field_id
                                                                                       )))
        username.send_keys("5105105105105100")

    # sending a valid month into the month text box
    def send_valid_month(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.month_field_id)))
        username.send_keys("March")

    # sending a valid year into the year text box
    def send_valid_year(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.year_field_id)))
        username.send_keys("2023")

    # sending an invalid name into the name text box
    def send_invalid_username(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.name_field_id)))
        username.send_keys("Khoth Voor"*3)

    # sending an invalid country into the country text box
    def send_invalid_country(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.country_field_id)))
        username.send_keys("Illuminen Alliance")

    # sending an invalid city into the city text box
    def send_invalid_city(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.city_field_id)))
        username.send_keys("Haseon")

    # sending an invalid credit card number into the credit card text box
    def send_invalid_credit_card_number(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.credit_card_field_id
                                                                                       )))
        username.send_keys("51051051050")

    # sending an invalid month into the month text box
    def send_invalid_month(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.month_field_id)))
        username.send_keys("aprimay")

    # sending an invalid year into the year text box
    def send_invalid_year(self):
        username = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID,
                                                                                       self.locator.year_field_id)))
        username.send_keys("25823")
