from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.drivers import ChromeDriver
driver = ChromeDriver().get_chrome_driver()

class HomepageElements:
    # find left arrow button in image of phones preview
    def find_image_slidebar_left_arrow(self):
        left_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                '//*[@id="carouselExampleIndicators"]/a[1]/span[1]')))

        return left_element

    # find right arrow button in image of phones preview
    def find_image_slidebar_right_arrow(self):
        right_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '//*[@id="carouselExampleIndicators"]/a[2]/span[1]')))

        return right_element

    # find "phones" button in category
    def find_category_phones_button(self):
        phone_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '/html/body/div[5]/div/div[1]/div/a[2]')))
        return phone_element

    # find "phones" image in category
    def find_category_phones_image(self):
        phone_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')))
        return phone_element

    # find "laptops" images in category
    def find_category_laptops_image(self):
        laptops_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                         '/html/body/div[5]/div/div[2]/div/div[1]/div/a/img')))
        return laptops_element

    # monitor category image
    def find_category_monitors_image(self):
        monitors_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                         '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img')))
        return monitors_element

    # find "laptops" button in category
    def find_category_laptops_button(self):
        laptops_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img')))

        return laptops_element

    # find "monitors" button in category
    def find_category_monitors_button(self):
        monitors_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                         '/html/body/div[5]/div/div[1]/div/a[4]')))

        return monitors_element

    # find samsung specific item button text link
    def find_item_samsung_galaxy_s6(self):
        samsung_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))

        return samsung_element

    # find "previous" button at the end of the homepage
    def find_previous_button(self):
        previous_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                         '/html/body/div[5]/div/div[2]/form/ul/li[1]/button')))

        return previous_element

    # find "next" button at the end of the homepage
    def find_next_button(self):
        next_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '/html/body/div[5]/div/div[2]/form/ul/li[2]/button')))

        return next_element

    # find "category" text in the homepage
    def find_category_text(self):
        category_text = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[1]/div/a[1]')))
        return category_text

    # find text price
    def find_phones_category_text_price(self):
        category_text = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[1]/div/div/p')))
        return category_text


    # find phones text in category
    def find_phones_text_description(self):
        phones_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[2]/div/div/p')))
        return phones_element

    # find phones text link
    def find_phones_link_text(self):
        phones_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))
        return phones_element

    # find laptops text description in category
    def find_laptops_text_description(self):
        phones_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))
        return phones_element

    # find monitors text description in category
    def find_monitors_text_description(self):
        phones_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[1]/div/div/p')))
        return phones_element

    # find monitors price text
    def find_monitors_text_price(self):
        phones_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h5')))
        return phones_element

    # monitors link text
    def find_monitors_link_text(self):
        phones_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))
        return phones_element

    # add item to cart button
    def find_items_add_to_cart(self):
        add_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div[2]/div/a')))

        return add_element

