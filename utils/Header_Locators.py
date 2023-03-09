from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.drivers import ChromeDriver

driver = ChromeDriver().get_chrome_driver()


class HeaderElements:
    # Pressing the signup button
    def pressing_sign_up_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "signin2")))

        return element

    # inserting the Username input
    def inserting_sign_up_user_name(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'sign-username')))

        return element

    # inserting the Password input
    def inserting_sign_up_password(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'sign-password')))

        return element

    # pressing the Signup button
    def pressing_sign_up_inner_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="signInModal'
                                                                                           '"]/div/div/div[3]/button['
                                                                                           '2]')))
        return element

    # pressing the Signup close button
    def pressing_sign_up_close_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[3]/button[1]")))

        return element

    # Pressing on the X button at the top right sign up
    def pressing_the_x_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[1]/button/span")))

        return element

    # pressing the Home button
    def pressing_home_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[1]/a")))

        return element

    # finding the contact email title text
    def find_contact_email_title(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                           "1]/div/div/div["
                                                                                           "2]/form/div[1]/label")))

        return element

    # find the " message title text"
    def find_message_title(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                           "1]/div/div/div["
                                                                                           "2]/form/div[3]/label")))

        return element

    # find the new message title text
    def find_new_message_title(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "exampleModalLabel")))

        return element

    # pressing the Contact button
    def pressing_contact_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[2]/a")))

        return element

    # inserting email input
    def insert_contact_email_input(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-email")))

        return element

    # inserting the contact name input
    def insert_contact_name_input(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "recipient-name")))

        return element

    # inserting the message input
    def insert_contact_message(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "message-text")))

        return element

    # pressing the "send message"
    def _pressing_send_contact_message(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                           "1]/div/div/div[3]/button["
                                                                                           "2]")))

        return element

    # pressing the close button at the contact section
    def pressing_the_close_button_contact(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/div["
                                                                                           "1]/div/div/div[3]/button["
                                                                                           "1]")))

        return element

    # Pressing the About us button

    def pressing_about_us_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/nav/div[1]/ul/li[3]/a")))

        return element

    # finding the video in the about us section
    def finding_about_us_video(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#example-video > "
                                                                                                  "div.vjs-poster")))

        return element

    # playing the video in the about us section
    def press_play_button_in_about_us(self):
        element = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#example-video > "
                                                                                              "button")))
        return element

    # pressing the close button in the about us section
    def pressing_about_us_close_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#videoModal > div > div > div.modal-footer > button")))

        return element

    # pressing Cart button
    def pressing_cart_button(self):
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#videoModal > div "
                                                                                                   "> div > "
                                                                                                   "div.modal-footer "
                                                                                                   "> button")))

        return element

    # Bug has been found - cannot click the button or locate from certain URL

    # find the products title in the cart section,
    # "Uncaught ReferenceError: showcart is not defined at HTMLAnchorElement.onclick (cart.html:716:63)
    # onclick @ cart.html:716"
    def find_products_title_cart(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-wrapper > "
                                                                                                  "div > div.col-lg-8"
                                                                                                  " > h2")))

        return element

    # find the total title text in the cart section
    def find_total_title_cart(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-wrapper > "
                                                                                                  "div > div.col-lg-1"
                                                                                                  " > h2")))

        return element

    # find pic column text in the cart section
    def find_pic_column_text_cart(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-wrapper > "
                                                                                                  "div > div.col-lg-8"
                                                                                                  " > div > table > "
                                                                                                  "thead > tr > "
                                                                                                  "th:nth-child(1)")))

        return element

    # find the "title" text on the cart section
    def find_title_text_cart(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-wrapper > "
                                                                                                  "div > div.col-lg-8"
                                                                                                  " > div > table > "
                                                                                                  "thead > tr > "
                                                                                                  "th:nth-child(2)")))

        return element

    # find the price text in the cart section

    def find_price_text_cart(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#page-wrapper > "
                                                                                                  "div > div.col-lg-8"
                                                                                                  " > div > table > "
                                                                                                  "thead > tr > "
                                                                                                  "th:nth-child(3)")))

        return element

    # pressing the cart place order button
    def pressing_cart_place_order_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#page-wrapper > div > div.col-lg-1 > button")))

        return element

    # removing an item from the cart
    def remove_item_from_cart(self):
        element = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tbodyid > tr > td:nth-child(4) > a")))

        return element

    #  pressing the login button
    def pressing_login_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "login2")))

        return element

    # inserting login username input
    def inserting_login_username(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "loginusername")))

        return element

    # inserting login password input
    def inserting_login_password(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "loginpassword")))

        return element

    # pressing the login  log in button
    def pressing_login_log_in_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[2]")))

        return element

    # pressing the login close button
    def pressing_login_close_button(self):
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]")))

        return element

    # finding the logo at the top left bar

    def find_logo_left_top_bar(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "/html/body/nav/a/img")))

        return element

    #  finding the Welcome <User> top right

    def find_welcome_user(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "nameofuser")))

        return element

    # pressing on the logout button

    def pressing_logout_button(self):
        element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "logout2")))

        return element


locators = HeaderElements()
driver.get("https://www.demoblaze.com/index.html")
driver.maximize_window()
click = locators.pressing_about_us_button()
click.click()
EC.element_to_be_clickable(locators.pressing_about_us_close_button())
