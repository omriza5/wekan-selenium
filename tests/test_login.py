import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)
        
    def tearDown(self):
        self.driver.quit()

    def test_page_health(self):
        self.login_page.open_page()
        self.login_page.enter_username('testuser')
        self.login_page.enter_password('testpassword')
        self.assertIn('sign-in', self.driver.current_url)
        self.login_page.click_login()
    
    def test_login_with_valid_credentials(self):
        self.login_page.open_page()
        self.login_page.enter_username('omriza5')
        self.login_page.enter_password('123456')
        self.login_page.click_login()
    
    def test_login_with_invalid_credentials(self):
        self.login_page.open_page()
        self.login_page.enter_username('invaliduser')
        self.login_page.enter_password('invalidpassword')
        self.login_page.click_login()

        error_message = self.login_page.get_login_error_message()
        self.assertIn('Login forbidden', error_message)
    
