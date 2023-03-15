# importing the necessary libraries
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# creating the method to get the chrome driver
def get_chrome_driver():
    chromedriver_path = "chromedriver.exe"
    service = Service(executable_path=chromedriver_path)
    options = Options()
    # setting the driver to disable all extensions for reliable testing
    options.add_argument("--disable-extensions")
    options.headless = False
    # getting the driver and returning it
    chrome_driver = webdriver.Chrome(service=service, options=options)
    return chrome_driver
