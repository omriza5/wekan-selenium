import unittest
from pages.board_page import BoardPage
from utils.driver_factory import get_driver

# For future tests
class TestBoard(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.board_page = BoardPage(self.driver)
        self.driver.implicitly_wait(10)
        
    