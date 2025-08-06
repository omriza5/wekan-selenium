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
    
    def test_example(self):
        """
        This method is an example test that checks if the home page is healthy.
        It verifies that the header is displayed.
        """
        login_page = LoginPage(self.driver)
        x=login_page.login_with_valid_credentials(
            self.home_page.username, 
            self.home_page.password, 
            Config.get_login_url()  
        )
        print(f"*********** open_page() returned: {type(x)}")
    # def test_home_page_health(self):
    #     """
    #     This method checks if the home page is healthy by verifying the title.
    #     """
    #     x = self.home_page.open_page()
    #     print(f"*********** open_page() returned: {type(x)}")
    #     header_element = self.home_page.is_header_displayed()
    #     self.assertTrue(header_element, "Header element is not displayed on the home page.")