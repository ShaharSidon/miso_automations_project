# importing the necessary libraries
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

# creating a class for finding the Chrome driver


class ChromeDriver:

    def __init__(self):
        chromedriver_path = "./chromedriver.exe"
        self.service = Service(executable_path=chromedriver_path)

    def get_chrome_driver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-extensions")
        chrome_driver = webdriver.Chrome(options=chrome_options)
        return chrome_driver
