import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPurchase(unittest.TestCase):
    # define a test case for purchasing with invalid credentials

    def setUp(self):
        # setup function to initialize the webdriver and open the target webpage
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/index.html")

    def tearDown(self):
        # teardown function to close the webdriver after the test completes
        self.driver.quit()

    def test_wrong_credentials(self):
        # define the test function for purchasing with invalid credentials
        # enter incorrect credentials
        name = "Test User"
        country = "Wrong Country"
        city = "Wrong City"
        card = "1234567890123456"
        month = "13"
        year = "2022"

        # locate purchase form elements and enter credentials
        cart = self.driver.find_element(By.ID, "cartur")  # locate the cart icon on the page
        cart.click()  # click the cart icon
        time.sleep(5)  # wait for 5 seconds to allow the cart page to load
        place_order = self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/button")  # locate the "Place
        # Order" button
        place_order.click()  # click the "Place Order" button
        time.sleep(5)  # wait for 5 seconds to allow the purchase modal to load
        name_input = self.driver.find_element(By.ID, "name")  # locate the input field for name
        name_input.send_keys(name)  # enter the name
        country_input = self.driver.find_element(By.ID, "country")  # locate the input field for country
        country_input.send_keys(country)  # enter the country
        city_input = self.driver.find_element(By.ID, "city")  # locate the input field for city
        city_input.send_keys(city)  # enter the city
        card_input = self.driver.find_element(By.ID, "card")  # locate the input field for card number
        card_input.send_keys(card)  # enter the card number
        month_input = self.driver.find_element(By.ID, "month")  # locate the input field for month
        month_input.send_keys(month)  # enter the month
        year_input = self.driver.find_element(By.ID, "year")  # locate the input field for year
        year_input.send_keys(year)  # enter the year
        purchase_submit_button = self.driver.find_element(By.CSS_SELECTOR,
                                                          "#orderModal > div > div > div.modal-footer > "
                                                          "button.btn.btn-primary")  # locate the "Purchase" button
        purchase_submit_button.click()  # click the "Purchase" button

        # verify that purchase is not completed
        cart_items = self.driver.find_elements(By.XPATH, "//tbody/tr")  # locate the cart items
        self.assertEqual(len(cart_items), 0)  # check if the cart is empty
        print("Test failed")


if __name__ == '__main__':
    unittest.main()
