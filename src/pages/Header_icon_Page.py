from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Header import HeaderLocators

class IconIsVisual:
    def __init__(self, driver):
        self.driver = driver

    def icon_is_visual(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HeaderLocators.product_store_xpath)))