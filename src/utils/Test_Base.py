import unittest
from src.utils.drivers import get_chrome_driver


class TestBaseHomepage(unittest.TestCase):
    """
    creating the setup and teardown for all the tests that start at the homepage
    """

    # creating the setup for the tests
    def setUp(self) -> None:
        try:
            self.driver = get_chrome_driver()
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get("https://www.demoblaze.com/index.html")
        except AssertionError:
            self.driver.quit()

    # creating the teardown for the tests
    def tearDown(self) -> None:
        self.driver.quit()


class TestBaseCart(unittest.TestCase):
    """
    creating the setup and teardown for all the tests that start at the cart page
    """

    # creating the setup for the tests
    def setUp(self) -> None:
        try:
            self.driver = get_chrome_driver()
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get("https://www.demoblaze.com/cart.html")
        except AssertionError:
            self.driver.quit()

    # creating the teardown for the tests
    def tearDown(self) -> None:
        self.driver.quit()
