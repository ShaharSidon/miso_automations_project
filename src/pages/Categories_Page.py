from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.Locators.Categories import CategoriesLocators

categories = CategoriesLocators()


class CategoriesPage:

    def __init__(self, driver):
        self.driver = driver

    def set_categories_title(self):
        categories_title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, categories.categories_title_xpath)))

    def click_on_phones(self):
        phones_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, categories.phones_button_xpath)))
        phones_btn.click()

    def click_on_monitors(self):
        monitors_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, categories.monitors_button_xpath)))
        monitors_btn.click()

    def click_on_laptops(self):
        laptops_btn = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, categories.phones_button_xpath)))
        laptops_btn.click()
