import unittest
from selenium import webdriver
from pages.board_page import BoardPage

# For future tests
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.board_page = BoardPage(self.driver)
        self.driver.implicitly_wait(10)
        
    