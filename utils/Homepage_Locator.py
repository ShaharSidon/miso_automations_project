from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomepageElements:
    def __init__(self, driver):
        self.driver = driver
    # find left arrow button in image of phones preview
    def find_image_slidebar_left_arrow(self):
        left_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '//*[@id="carouselExampleIndicators"]/a[1]/span[1]')))

        return left_element

    # find right arrow button in image of phones preview
    def find_image_slidebar_right_arrow(self):
        right_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '//*[@id="carouselExampleIndicators"]/a[2]/span[1]')))

        return right_element

    # find "phones" button in category
    def find_category_phones_button(self):
        phone_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '/html/body/div[5]/div/div[1]/div/a[2]')))
        return phone_element

    # monitor category image
    def find_category_image(self):
        image_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                         '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img')))
        return image_element

    # find "laptops" button in category
    def find_category_laptops_button(self):
        laptops_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[5]/div/div[2]/div/div[2]/div/a/img')))

        return laptops_element

    # find "monitors" button in category
    def find_category_monitors_button(self):
        monitors_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                         '/html/body/div[5]/div/div[1]/div/a[4]')))

        return monitors_element

    # find samsung specific item button text link
    def find_item_samsung_galaxy_s6(self):
        samsung_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                        '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))

        return samsung_element

    # find "previous" button at the end of the homepage
    def find_previous_button(self):
        previous_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                         '/html/body/div[5]/div/div[2]/form/ul/li[1]/button')))

        return previous_element

    # find "next" button at the end of the homepage
    def find_next_button(self):
        next_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                      '/html/body/div[5]/div/div[2]/form/ul/li[2]/button')))

        return next_element

    # find "category" text in the homepage
    def find_category_text(self):
        category_text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[1]/div/a[1]')))
        return category_text

    # find text price
    def find_category_item_text_price(self):
        category_text = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[1]/div/div/p')))
        return category_text


    # find item description text in category
    def find_category_item_text_description(self):
        category_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[2]/div/div/p')))
        return category_element

    # find category item text link
    def find_category_item_link_text(self):
        category_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                       '/html/body/div[5]/div/div[2]/div/div[1]/div/div/h4/a')))
        return category_element

    # add item to cart button
    def find_items_add_to_cart(self):
        add_element = WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH,
                                                                                          '/html/body/div[5]/div/div[2]/div[2]/div/a')))

        return add_element

