import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config import Config

URL_PATH = 'sign-in'
TEST_USERNAME = 'testUsername'
TEST_PASSWORD = 'testPassword'
VALID_USERNAME = 'omriza5@gmail.com'
VALID_PASSWORD = '123456'
LOGIN_ERROR_MESSAGE = 'Login forbidden'
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)
        
    def tearDown(self):
        self.driver.quit()

    def test_page_health(self):
        self.login_page.open_page(Config.get_login_url())
        self.assertIn(URL_PATH, self.driver.current_url)
        
    def test_login_with_valid_credentials(self):
        self.login_page.open_page(Config.get_login_url())
        self.login_page.enter_username(VALID_USERNAME)
        self.login_page.enter_password(VALID_PASSWORD)
        self.login_page.click_login()
    
    def test_login_with_invalid_credentials(self):
        self.login_page.open_page(Config.get_login_url())
        self.login_page.enter_username(TEST_USERNAME)
        self.login_page.enter_password(TEST_PASSWORD)
        self.login_page.click_login()

        error_message = self.login_page.get_login_error_message()
        self.assertIn(LOGIN_ERROR_MESSAGE, error_message)
    
