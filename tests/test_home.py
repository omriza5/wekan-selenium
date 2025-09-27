import unittest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.config import Config
from utils.driver_factory import get_driver
from utils.page_factory import get_board_page   
  
class TestHome(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.home_page = HomePage(self.driver)
        self.board_page = get_board_page(self.driver, Config.screen_width())
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
        
        self.assertEqual(type(board_page).__name__, type(self.board_page).__name__, "board_page is not an instance of BoardPage")
    
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
                      .add_list("In Progress")
                      .add_card_to_bottom("To Do", "Implement feature X"))

        # Verify the card was added
        card_titles = board_page.get_list_cards_titles("To Do")
        self.assertIn("Implement feature X", card_titles, "Card was not added to the list.")
          
    def test_member_setting_menu_open(self):
        """
        This method tests the member settings menu functionality.
        """
        login_page = LoginPage(self.driver)
        home_page = (login_page
                      .login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
                      .open_member_settings_menu())
        
        # check if the member settings menu is displayed as a popup             
        is_menu_displayed = home_page.is_member_settings_menu_displayed()
        self.assertTrue(is_menu_displayed, "Member settings menu is not displayed.")
    
    def test_member_setting_menu_close(self):
        """
        This method tests the member settings menu functionality.
        """
        login_page = LoginPage(self.driver)
        home_page = (login_page
                      .login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
                      .open_member_settings_menu()
                      .close_member_settings_menu())
                        
        # Verify the member color was changed
        is_menu_displayed = home_page.is_member_settings_menu_displayed()
        self.assertFalse(is_menu_displayed, "Member settings menu is still displayed.")
    
    def test_notifications_menu_open(self):
        """
        This method tests the notifications menu functionality.
        """
        login_page = LoginPage(self.driver)
        home_page = (login_page
                      .login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
                      .open_notifications_menu())
                           
        is_menu_displayed = home_page.is_notifications_menu_displayed()
        self.assertTrue(is_menu_displayed, "Notifications menu is not displayed.")
        
    def test_notifications_menu_close(self):
        """
        This method tests the notifications menu functionality.
        """
        login_page = LoginPage(self.driver)
        home_page = (login_page
                      .login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
                      .open_notifications_menu()
                      .close_notifications_menu())
                           
        is_menu_displayed = home_page.is_notifications_menu_displayed()
        self.assertFalse(is_menu_displayed, "Notifications menu is still displayed.")

    def test_logout(self):
        """
        This method tests the logout functionality.
        """
        login_page = LoginPage(self.driver)
        login_page = (login_page
                      .login_with_valid_credentials(Config.VALID_USERNAME, Config.VALID_PASSWORD, Config.get_login_url())
                      .logout())
        self.assertIsInstance(login_page, LoginPage, "Logout did not navigate to login page.")
