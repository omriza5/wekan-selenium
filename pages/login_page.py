import time
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, 'at-field-username_and_email')
        self.password_textbox = (By.ID, 'at-field-password')
        self.login_button = (By.ID, 'at-btn')
    
    def open_page(self, url):
        self.driver.get(url)
    
    def enter_username(self, username):
        username_field = self.driver.find_element(*self.username_textbox)
        username_field.clear()
        username_field.send_keys(username)
    
    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_textbox)
        password_field.clear()
        password_field.send_keys(password)
    
    def click_login(self):
        login_button = self.driver.find_element(*self.login_button)
        login_button.click()
    
    def get_login_error_message(self):
        error_message = self.driver.find_element(By.XPATH, "//p[contains(text(), 'Login forbidden')]")
        return error_message.text if error_message else None

    def login_with_valid_credentials(self, username, password, url):
        self.open_page(url)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
    
        # Lazy import to avoid circular dependency
        from pages.home_page import HomePage
        time.sleep(2)
        return HomePage(self.driver)