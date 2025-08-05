import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages.home_page import HomePage

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.home_page = HomePage(self.driver)
        self.driver.implicitly_wait(10)
    
    def tearDown(self):
        self.driver.quit()
    
    def test_home_page_health(self):
        """
        This method checks if the home page is healthy by verifying the title.
        """
        self.home_page.open_page()
        header_element = self.home_page.is_header_displayed()
        self.assertTrue(header_element, "Header element is not displayed on the home page.")