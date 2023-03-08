from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.drivers import ChromeDriver
driver = ChromeDriver().get_chrome_driver()

class HomepageElements:
    #left arrow button
    def image_slidebar_left_arrow(self):
        left_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH,
                                                                                '//*[@id="carouselExampleIndicators"]/a[1]/span[1]'))

        return left_element

    # right arrow button
    def image_slidebar_right_arrow(self):
        right_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH,
                                                                                      '//*[@id="carouselExampleIndicators"]/a[2]/span[1]'))

        return right_element

    # phones button in category
    def category_phones_button(self):
        phone_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH,
                                                                                      '/html/body/div[5]/div/div[1]/div/a[2]'))

        return phone_element

    # laptops button in category
    def category_laptops_button(self):
        laptops_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH,
                                                                                        '/html/body/div[5]/div/div[1]/div/a[3]'))

        return laptops_element

    # monitors button in category
    def category_monitors_button(self):
        monitors_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH,
                                                                                         '/html/body/div[5]/div/div[1]/div/a[4]'))

        return monitors_element

    # item button text link
    def item_samsung_galaxy_s6(self):
        samsung_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH,
                                                                                        '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a'))

        return samsung_element

    # previous button
    def previous_button(self):
        previous_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH,
                                                                                         '/html/body/div[5]/div/div[2]/form/ul/li[1]/button'))

        return previous_element

    # next button
    def next_button(self):
        next_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(By.XPATH, '/html/body/div[5]/div/div[2]/form/ul/li[2]/button'))

        return next_element

