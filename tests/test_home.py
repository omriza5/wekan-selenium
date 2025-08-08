import unittest
from selenium import webdriver
import time
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import Config
from pages.board_page import BoardPage
from utils.selenium_config import get_chrome_options

class TestLogin(unittest.TestCase):
    def setUp(self):
        options = get_chrome_options()
        self.driver = webdriver.Chrome(options=options)
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
    
    def test_board_creation(self):
        """
        This method tests the creation of a board.
        """
        login_page = LoginPage(self.driver)
        board_page = (login_page
                      .login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
                      .create_board("Test Board"))
        self.assertIsInstance(board_page, BoardPage, "board_page is not an instance of BoardPage")
    
    def test_add_list_to_board(self):
        """
        This method tests adding a list to a board.
        """
        login_page = LoginPage(self.driver)
        board_page = (login_page
                      .login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
                      .create_board("Test Board - with lists")
                      .add_list("To Do")
                      .add_list("In Progress")
                      .add_list("Done"))
        
        list_names = board_page.get_list_names()
        for expected in ["To Do", "In Progress", "Done"]:
            self.assertIn(expected, list_names, f"List '{expected}' was not found on the board.")
            
    def test_add_card_to_list(self):
        """
        This method tests adding a card to a list.
        """
        login_page = LoginPage(self.driver)
        board_page = (login_page
                      .login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
                      .create_board("Test Board")
                      .add_list("To Do")
                      .add_card_to_bottom("To Do", "Implement feature X"))

        # Verify the card was added
        card_titles = board_page.get_list_cards_titles("To Do")
        self.assertIn("Implement feature X", card_titles, "Card was not added to the list.")
