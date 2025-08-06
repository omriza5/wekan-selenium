import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import Config

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.driver.implicitly_wait(10)
    
    def tearDown(self):
        self.driver.quit()
    
    def test_page_health(self):
        """
        This method checks if the home page is healthy by verifying the title.
        """
        login_page = LoginPage(self.driver)
        login_page.login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
        self.assertTrue(self.home_page.is_header_displayed(), "Header is not displayed on the home page.")
