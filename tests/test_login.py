import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import Config

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)
        
    def tearDown(self):
        self.driver.quit()

    def test_page_health(self):
        self.login_page.open_page(Config.get_login_url())
        self.assertIn(Config.URL_PATH, self.driver.current_url)

    def test_login_with_valid_credentials(self):
        self.login_page.open_page(Config.get_login_url())
        self.login_page.enter_username(Config.VALID_USERNAME)
        self.login_page.enter_password(Config.VALID_PASSWORD)
        self.login_page.click_login()
    
    def test_login_with_invalid_credentials(self):
        self.login_page.open_page(Config.get_login_url())
        self.login_page.enter_username(Config.TEST_USERNAME)
        self.login_page.enter_password(Config.TEST_PASSWORD)
        self.login_page.click_login()

        error_message = self.login_page.get_login_error_message()
        self.assertIn(Config.LOGIN_ERROR_MESSAGE, error_message)
    
