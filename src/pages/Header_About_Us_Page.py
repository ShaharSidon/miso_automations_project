from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.About_Us import AboutUs

class About_us_page:

    def __init__(self, driver):
        self.driver = driver

    def about_us_click_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, AboutUs.x_button_xpath))).click()

    def about_us_play_video(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, AboutUs.play_button_xpath))).click()

    def about_us_close_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, AboutUs.close_xpath))).click()

    def about_us_ui_visable(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, AboutUs.about_us_title)))
