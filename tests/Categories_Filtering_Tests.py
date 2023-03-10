# importing the necessary libraries
import unittest
from utils.drivers import get_chrome_driver
from utils.Homepage_Locator import HomepageElements


# creating the class for the tests
class TestingFilteringByCategories(unittest.TestCase):
    # creating the setup for the tests
    def setUp(self):
        # attempt to do the following actions
        try:
            self.driver = get_chrome_driver()
            self.driver.implicitly_wait(5)
            self.driver.get("https://www.demoblaze.com/index.html")
            self.driver.maximize_window()
            self.locator = HomepageElements(self.driver)
        # if you discovered a AssertionError do this
        except AssertionError:
            self.driver.quit()

    # creating the teardown for the tests
    def tearDown(self):
        self.driver.quit()

    # the start of the first test:
    def test_1_filter_by_phones(self):
        # find the filter button for phones and press it
        button = self.locator.find_category_phones_button()
        button.click()
        # wait for the page to update and make sure that a change happened
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html#"
        # get the name of a product and check that the name displayed is the name that should be there
        # according to the filter
        phone = self.locator.find_category_item_link_text().get_attribute("innerText")
        assert phone == "Samsung galaxy s6"

    # the start of the second test:
    def test_2_filter_by_laptops(self):
        # find the filter button for phones and press it
        button = self.locator.find_category_laptops_button()
        button.click()
        # wait for the page to update and make sure that a change happened
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html#"
        # get the name of a product and check that the name displayed is the name that should be there
        # according to the filter
        phone = self.locator.find_category_item_link_text().get_attribute("innerText")
        assert phone == "Sony vaio i5"

    # the start of the second test:
    def test_3_filter_by_monitors(self):
        # find the filter button for phones and press it
        button = self.locator.find_category_monitors_button()
        button.click()
        # wait for the page to update and make sure that a change happened
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == "https://www.demoblaze.com/index.html#"
        # get the name of a product and check that the name displayed is the name that should be there
        # according to the filter
        phone = self.locator.find_category_item_link_text().get_attribute("innerText")
        assert phone == "Apple monitor 24"
