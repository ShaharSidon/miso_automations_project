from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.drivers import ChromeDriver
driver = ChromeDriver().get_chrome_driver()


# creating the class that will contain all the footer locators
class FooterElements:

    # creating a method to find the locator of the about us title
    def find_the_about_us_title(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 '#fotcont > div:nth-child(1) > div > '
                                                                                 'div > h4 > b')))
        return element

    # creating a method to find the locator of the about us text
    def find_the_about_us_text(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 '#fotcont > div:nth-child(1) > div > '
                                                                                 'div > p')))
        return element

    # creating a method to find the locator of the get in touch title
    def find_the_get_in_touch_title(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 '#fotcont > div.col-sm-3.col-lg-3.col'
                                                                                 '-md-3 > div > div > h4 > b')))
        return element

    # creating a method to find the locator of the address text
    def find_the_address_text(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 '#fotcont > div.col-sm-3.col-lg-3.col'
                                                                                 '-md-3 > div > div > p:nth-child(2)')))
        return element

    # creating a method to find the locator of the phone text
    def find_the_phone_text(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 '#fotcont > div.col-sm-3.col-lg-3.col'
                                                                                 '-md-3 > div > div > p:nth-child(3)')))
        return element

    # creating a method to find the locator of the email text
    def find_the_email_text(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 '#fotcont > div.col-sm-3.col-lg-3.col'
                                                                                 '-md-3 > div > div > p:nth-child(4)')))
        return element

    # creating a method to find the locator of the store logo
    def find_the_store_logo(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 '#fotcont > div:nth-child(3) > div > '
                                                                                 'div > h4 > img')))
        return element

    # creating a method to find the locator of the store name
    def find_the_store_name(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 '#fotcont > div:nth-child(3) > div > '
                                                                                 'div > h4')))
        return element

    # creating a method to find the locator of the copyright text
    def find_the_copyright_text(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                 'body > footer > p')))
        return element
