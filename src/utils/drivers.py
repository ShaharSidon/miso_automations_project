# importing the necessary libraries
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# creating a class for finding the Chrome driver


class ChromeDriver:
    # defining where the chrome driver is located and what service is equal to
    def __init__(self):
        chromedriver_path = "chromedriver.exe"
        self.service = Service(executable_path=chromedriver_path)

    # creating the method to get the chrome driver
    def get_chrome_driver(self):
        chrome_options = webdriver.ChromeOptions()
        # setting the driver to disable all extensions for reliable testing
        chrome_options.add_argument("--disable-extensions")
        # getting the driver and returning it
        chrome_driver = webdriver.Chrome(options=chrome_options)
        return chrome_driver
