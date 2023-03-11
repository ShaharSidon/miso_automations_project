import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestDemoBlaze(unittest.TestCase):
    # TS 51 Verifying that when clicking the categories button it leads to desired page
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_categories_page(self):
        # Click the Categories link
        self.driver.find_element(By.CSS_SELECTOR, "#cat").click()
        time.sleep(5)

        # Verify that we are on the Categories page
        categories_page = self.driver.current_url
        expected_page = "https://www.demoblaze.com/index.html"

        self.assertIn(expected_page, categories_page)


if __name__ == '__main__':
    unittest.main()
