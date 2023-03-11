# importing the necessary libraries
import unittest
from utils.drivers import ChromeDriver
from utils.Homepage_Locator import HomepageElements
from utils.Header_Locators import HeaderElements


# creating the class for the tests
class RemovingAnItem(unittest.TestCase):
    # creating the setup for the tests
    def setUp(self) -> None:
        self.driver = ChromeDriver().get_chrome_driver()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()
        self.first_locator = HomepageElements(self.driver)
        self.second_locator = HeaderElements(self.driver)

    # creating the teardown for the tests
    def tearDown(self) -> None:
        self.driver.quit()

    def test_1_removing_an_item_from_the_cart(self):
        first_button = self.first_locator.find_category_item_link_text()
        first_button.click()
        second_button = self.first_locator.find_items_add_to_cart()
        second_button.click()
        third_button = self.second_locator.pressing_cart_button()
        third_button.click()
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html"
        fourth_button = self.second_locator.remove_item_from_cart()
        fourth_button.click()
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html#"

