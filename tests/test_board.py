import unittest
from selenium import webdriver
from pages.board_page import BoardPage
from utils.selenium_config import get_chrome_options

# For future tests
class TestBoard(unittest.TestCase):
    def setUp(self):
        options = get_chrome_options()
        self.driver = webdriver.Chrome(options=options)
        self.board_page = BoardPage(self.driver)
        self.driver.implicitly_wait(10)
        
    