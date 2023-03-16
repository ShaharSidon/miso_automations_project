from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Homepage_Locators import Homepage_Locators

# page actions of all items in homepage
class HomepageItems:
    def __init__(self, driver):
        self.driver = driver
    def nokia_lumina_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.nokia_lumina_1520_image_xpath))).click()

    def nexus_6_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.nexus_6_image_xpath))).click()

    def samsung_galaxy_s7_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.samsung_galaxy_s7_image_xpath))).click()

    def iphone_6_32gb_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.iphone_6_32gb_image_xpath))).click()

    def sony_xperia_z5_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.sony_xperia_z5_link_xpath))).click()

    def HTC_one_m9_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.HTC_one_m9_image_xpath))).click()

    def sony_vaio_i5_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.sony_vaio_i5_link_xpath))).click()

    def sony_vaio_i7_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.sony_vaio_i7_image_xpath))).click()

    def apple_monitor_24_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.apple_monitor_24_image_xpath))).click()

    def macbook_air_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.macbook_air_image_xpath))).click()

    def dell_i7_8gb_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.dell_i7_8gb_image_xpath))).click()

    def laptop_2017_dell_15_inch_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.laptop_2017_dell_15_inch_image_xpath))).click()

    def asus_full_hd_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.asus_full_hd_image_xpath))).click()

    def macbook_pro_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.macbook_pro_image_xpath))).click()

    def next_buton(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.macbook_pro_image_xpath))).click()

    def previous_buton(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Homepage_Locators.macbook_pro_image_xpath))).click()

