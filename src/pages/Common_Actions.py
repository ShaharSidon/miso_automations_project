# importing the necessary libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# creating the class for the common actions
class CommonActions:
    # defining the inputs for the class
    def __init__(self, locator, driver):
        self.locator = f'{locator}'
        self.driver = driver

    # writing a click action that uses a css locator
    def click_element_css(self):
        button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator)))
        button.click()

    # writing a click action that uses a xpath locator
    def click_element_xpath(self):
        button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.locator)))
        button.click()

    # writing a click action that uses an id locator
    def click_element_id(self):
        button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, self.locator)))
        button.click()

    # writing a functions that finds the inner text of a css locator
    def get_inner_text_css(self):
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator)))
        inner_text = element.get_attribute("innerText")
        return inner_text

    # writing a functions that finds the inner text of a xpath locator
    def get_inner_text_xpath(self):
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.locator)))
        inner_text = element.get_attribute("innerText")
        return inner_text

    # writing a functions that finds the inner text of an id locator
    def get_inner_text_id(self):
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, self.locator)))
        inner_text = element.get_attribute("innerText")
        return inner_text

    # writing a functions that finds the source of an image using a css locator
    def get_photo_src_css(self):
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.locator)))
        source = element.get_attribute("src")
        return source

    # writing a functions that finds the source of an image using a xpath locator
    def get_photo_src_xpath(self):
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, self.locator)))
        source = element.get_attribute("src")
        return source

    # writing a functions that finds the source of an image using an id locator
    def get_photo_src_id(self):
        element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.ID, self.locator)))
        source = element.get_attribute("src")
        return source
