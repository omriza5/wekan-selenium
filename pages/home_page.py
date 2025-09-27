from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.screenshot import take_screenshot
from utils.page_factory import get_board_page
from utils.config import Config
from pages.login_page import LoginPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.page_board = get_board_page(driver, Config.screen_width())
        self.header_main_bar = (By.ID, "header-main-bar")
        self.username = "omriza5@gmail.com"
        self.password = "123456"
        self.add_board_link = (By.CLASS_NAME, "js-add-board")
        self.board_title_textbox = (By.CLASS_NAME, "js-new-board-title")
        self.add_board_btn = (By.XPATH, "//input[translate(@value, 'CREATE', 'create')='create']")
        self.member_menu_open_btn = (By.CLASS_NAME, "header-user-bar-avatar")
        self.member_menu_close_btn = (By.CLASS_NAME, "close-btn.js-close-pop-over")
        self.member_settings_title = (By.XPATH, "//span[@class='header-title']")
        self.notification_section = (By.ID,'notifications-drawer')
        self.notifications_menu_open_btn = (By.ID, "notifications")
        self.notifications_menu_close_btn = (By.CLASS_NAME, "fa.fa-times-thin.close")
        self.logout_btn = (By.CLASS_NAME, "js-logout")
    
    def is_header_displayed(self):
        """
        This method checks if the header is displayed on the home page.
        """
        try:
            header_element = self.driver.find_element(*self.header_main_bar)
            return header_element.is_displayed()
        except Exception as e:      
            print(f"Error in is_header_displayed: {e}")
    
    def create_board(self, board_title):
        try:
            # Wait for the "Add Board" link to be clickable
            self.driver.implicitly_wait(10)
            # Directly find and click the "Add Board" link
            board_link = self.driver.find_element(*self.add_board_link)
            board_link.click()
            
            # Find and fill the board title field
            board_title_field = self.driver.find_element(*self.board_title_textbox)
            board_title_field.clear()
            board_title_field.send_keys(board_title)
            
            board_add_btn = self.driver.find_element(*self.add_board_btn)
            board_add_btn.click()
            
            return self.page_board
        except Exception as e:
            take_screenshot(self.driver, "error_during_board_creation")
        
    def open_member_settings_menu(self):
        try:
            member_menu_btn = self.driver.find_element(*self.member_menu_open_btn)
            member_menu_btn.click()
            return self
        except Exception as e:
            print(f"Error in open_member_settings_menu: {e}")

    def close_member_settings_menu(self):
        try:
            close_btn = self.driver.find_element(*self.member_menu_close_btn)
            close_btn.click()
            return self
        except Exception as e:
            print(f"Error in close_member_settings_menu: {e}")
            
    def is_member_settings_menu_displayed(self):
        try:
            # menu_title = self.driver.find_element(*self.member_settings_title)
            menu_title = self.wait.until(
                EC.visibility_of_element_located(self.member_settings_title)
            )
            return menu_title.is_displayed()
        except Exception as e:
            print(f"Error in is_member_settings_menu_displayed: {e}")
    
    def open_notifications_menu(self):
        try:
            notifications_btn = self.driver.find_element(*self.notifications_menu_open_btn)
            notifications_btn.click()
            return self
        except Exception as e:
            print(f"Error in open_notifications_menu: {e}")
            
    def close_notifications_menu(self):
        try:
            notifications_btn = self.driver.find_element(*self.notifications_menu_close_btn)
            notifications_btn.click()
            return self
        except Exception as e:
            print(f"Error in open_notifications_menu: {e}")
            
    def is_notifications_menu_displayed(self):
        try:
            notifications_section = self.driver.find_element(*self.notification_section)
            return notifications_section.is_displayed()
        except Exception as e:
            print(f"Error in is_notifications_menu_displayed: {e}")
    
    def logout(self):
        try:
            self.open_member_settings_menu()
            logout_btn = self.driver.find_element(*self.logout_btn)
            logout_btn.click()
            return LoginPage(self.driver)
        except Exception as e:
            print(f"Error in logout: {e}")



