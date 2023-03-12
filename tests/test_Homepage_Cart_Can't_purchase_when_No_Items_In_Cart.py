import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Create a test case class that inherits from unittest.TestCase
class PurchasingWithAnEmptyCart(unittest.TestCase):

    # Define a setUp method that will be executed before each test method
    def setUp(self):
        # Create a new instance of the Chrome driver and maximize the window
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # Navigate to the demo site
        self.driver.get("https://www.demoblaze.com/index.html")

    # Define a test method that tests the purchase with empty cart scenario
    def test_purchase_with_empty_cart(self):
        # Click on cart icon
        self.driver.find_element(By.ID, "cartur").click()

        # Verify that the cart is empty
        cart_items = self.driver.find_elements(By.XPATH, "//table[@class='table table-bordered table-hover']/tbody/tr")
        self.assertEqual(len(cart_items), 0, "Cart is not empty")

        # Click on the "Place Order" button
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button").click()

    # Define a tearDown method that will be executed after each test method
    def tearDown(self):
        # Quit the driver instance
        self.driver.quit()


# If this script is executed directly, run the test case using unittest.main()
if __name__ == '__main__':
    unittest.main()
