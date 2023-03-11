from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium import webdriver
import time


class TestDemoBlaze(unittest.TestCase):
    # TS52 Verifying that the video in the about us section is running properly

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.demoblaze.com/index.html")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_about_us_video(self):
        # Click the About us section
        self.driver.find_element(By.LINK_TEXT, "About us").click()

        # Click the play button
        play_button = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/button")
        play_button.click()

        # Wait for the video to start playing
        time.sleep(5)

        # Verify that the video is playing
        video = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/form/div/div/video")
        self.assertTrue(video.is_displayed())
        self.assertNotEqual(video.get_attribute("currentTime"), 0)
