import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.board_page import BoardPage
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.header_main_bar = (By.ID, "header-main-bar")
        self.username = "omriza5@gmail.com"
        self.password = "123456"
        self.add_board_link = (By.CLASS_NAME, "js-add-board")
        self.board_title_textbox = (By.CLASS_NAME, "js-new-board-title")
        self.add_board_btn = (By.CSS_SELECTOR, "input[value='Create']")
    
    def is_header_displayed(self):
        """
        This method checks if the header is displayed on the home page.
        """
        header_element = self.driver.find_element(*self.header_main_bar)
        return header_element.is_displayed()
    
    def create_board(self, board_title):
        try:
            # Directly find and click the "Add Board" link
            board_link = self.driver.find_element(*self.add_board_link)
            print(f"Clicking on the 'Add Board' link: {board_link.text}")
            board_link.click()
            
            # Find and fill the board title field
            board_title_field = self.driver.find_element(*self.board_title_textbox)
            board_title_field.clear()
            board_title_field.send_keys(board_title)
            
            # Directly find and click the "Create" button
            board_add_btn = self.driver.find_element(*self.add_board_btn)
            board_add_btn.click()
            
            return BoardPage(self.driver)
        except Exception as e:
            print(f"Error occurred: {str(e)}")  # Get the error message
            print(f"Error details: {repr(e)}")  # Get detailed error info
            print(f"Error arguments: {e.args}")  # Get the arguments passed to the exception
            traceback.print_exc()


