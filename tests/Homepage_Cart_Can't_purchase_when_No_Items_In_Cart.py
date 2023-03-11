import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestDemoBlaze(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")

    def test_purchase_with_empty_cart(self):
        # Click on cart icon
        self.driver.find_element(By.ID, "cartur").click()

        # Verify that the cart is empty
        cart_items = self.driver.find_elements(By.XPATH, "//table[@class='table table-bordered table-hover']/tbody/tr")
        self.assertEqual(len(cart_items), 0, "Cart is not empty")

        # Click on the "Place Order" button
        self.driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]").click()

        # Wait for the error message to appear
        error_msg = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='sweet-alert showSweetAlert visible']/p"))
        )

        # Verify that the error message is displayed
        self.assertEqual(error_msg.text, "Please add some products to your cart!", "Error message not displayed")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
