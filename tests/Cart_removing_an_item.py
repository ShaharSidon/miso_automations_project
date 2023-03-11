# importing the necessary libraries
import unittest
from utils.drivers import ChromeDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# creating the class for the tests
class RemovingAnItem(unittest.TestCase):
    # creating the setup for the tests
    def setUp(self) -> None:
        self.driver = ChromeDriver().get_chrome_driver()
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.maximize_window()

    # creating the teardown for the tests
    def tearDown(self) -> None:
        self.driver.quit()

    def test_1_removing_an_item_from_the_cart(self):
        first_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                           '/html/body/div[5]/div/'
                                                                                           'div[2]/div/div[1]/div/'
                                                                                           'div/h4')))
        first_button.click()
        second_button = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                            '/html/body/div['
                                                                                            '5]/div/div[2]/div['
                                                                                            '2]/div/a')))
        second_button.click()
        third_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#cartur"
                                                                                            )))
        third_button.click()
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html"
        fourth_button = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#tbodyid > "
                                                                                                         "tr > "
                                                                                                         "td:nth"
                                                                                                         "-child(4) > "
                                                                                                         "a")))
        fourth_button.click()
        assert self.driver.current_url == "https://www.demoblaze.com/cart.html#"

