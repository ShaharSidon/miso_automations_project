import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPurchase(unittest.TestCase):
    # TS 56 Ordering with invalid credentials

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")

    def tearDown(self):
        self.driver.quit()

    def test_wrong_credentials(self):
        # enter incorrect credentials
        name = "Test User"
        country = "Wrong Country"
        city = "Wrong City"
        card = "1234567890123456"
        month = "13"
        year = "2022"

        # locate purchase form elements and enter credentials
        cart = self.driver.find_element(By.ID, "cartur")
        cart.click()
        time.sleep(5)
        place_order = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button")
        place_order.click()
        time.sleep(5)
        name_input = self.driver.find_element(By.ID, "name")
        name_input.send_keys(name)
        country_input = self.driver.find_element(By.ID, "country")
        country_input.send_keys(country)
        city_input = self.driver.find_element(By.ID, "city")
        city_input.send_keys(city)
        card_input = self.driver.find_element(By.ID, "card")
        card_input.send_keys(card)
        month_input = self.driver.find_element(By.ID, "month")
        month_input.send_keys(month)
        year_input = self.driver.find_element(By.ID, "year")
        year_input.send_keys(year)
        purchase_submit_button = self.driver.find_element(By.CSS_SELECTOR,
                                                          "#orderModal > div > div > div.modal-footer > "
                                                          "button.btn.btn-primary")
        purchase_submit_button.click()

        # verify that an error message is displayed and purchase is not completed
        error_message = self.driver.find_element("//div[@class='sweet-alert showSweetAlert visible']/p")
        self.assertEqual(error_message.text, "Please fill out Name and Creditcard.")
        cart_items = self.driver.find_elements(By.XPATH, "//tbody/tr")
        self.assertEqual(len(cart_items), 0)
        print("Test failed")


if __name__ == '__main__':
    unittest.main()
