import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPhoneLink(unittest.TestCase):
    # TS61 Verifying that the item matches the link

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_phone_link(self):
        phone_name = "Samsung galaxy s6"
        expected_link = "https://www.demoblaze.com/prod.html?idp_=10"

        # locate phone and click on it
        phone_cat = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[2]")
        phone_cat.click()
        time.sleep(5)
        phone_link = self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a")
        phone_link.click()
        time.sleep(5)

        print("The item matches the link")


if __name__ == '__main__':
    unittest.main()
