from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Footer import FooterLocators

class Footer_Page:
    def __init__(self, driver):
        self.driver = driver

    def footer_is_visual_about_us_title(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.about_us_title))).click()

    def footer_is_visual_about_us_txt(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.about_us_txt))).click()

    def footer_is_visual_get_in_touch_title(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.get_in_touch_title))).click()

    def footer_is_visual_address_text(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.address_txt))).click()

    def footer_is_visual_phone_txt(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.phone_txt))).click()

    def footer_is_visual_email_txt(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.email_txt))).click()

    def footer_is_visual_product_store_title(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.product_store_title))).click()

    def footer_is_visual_logo_pic(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.logo_pic))).click()

    def footer_is_visual_copy_right_txt(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, FooterLocators.copy_right_txt))).click()


        