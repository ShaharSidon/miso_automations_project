import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class ClickTheMonitorsNextAndPreviousPage(unittest.TestCase):
    # Test Suite 49: Clicking the next page button in the monitors section
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_monitor_page(self):
        # Click the Laptops category link
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]").click()

        # Verify that we are on the Monitors page
        assert self.driver.current_url == "https://www.demoblaze.com/index.html#"

    # Test Suite 50: Clicking the previous page button in the monitors section

    def test_previous_monitors_page(self):
        # Click the Laptops category link
        self.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/a[3]").click()

        # Get the current page URL
        current_url = self.driver.current_url

        # Click the "Previous" button
        self.driver.find_element(By.CSS_SELECTOR, "#prev2").click()

        # Verify that we are back on the previous monitors page
        prev_url = self.driver.current_url

        self.assertEqual(current_url, prev_url)


if __name__ == '__main__':
    unittest.main()
