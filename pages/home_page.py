from selenium.webdriver.common.by import By
from pages.board_page import BoardPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.header_main_bar = (By.ID, "header-main-bar")
        self.username = "omriza5@gmail.com"
        self.password = "123456"
        self.add_board_link = (By.CLASS_NAME, "js-add-board")
        self.board_title_textbox = (By.CLASS_NAME, "js-new-board-title")
        self.add_board_btn = (By.XPATH, "//input[translate(@value, 'CREATE', 'create')='create']")
    
    def is_header_displayed(self):
        """
        This method checks if the header is displayed on the home page.
        """
        header_element = self.driver.find_element(*self.header_main_bar)
        return header_element.is_displayed()
    
    def create_board(self, board_title):
        # Directly find and click the "Add Board" link
        board_link = self.driver.find_element(*self.add_board_link)
        board_link.click()
        
        # Find and fill the board title field
        board_title_field = self.driver.find_element(*self.board_title_textbox)
        board_title_field.clear()
        board_title_field.send_keys(board_title)
        
        board_add_btn = self.driver.find_element(*self.add_board_btn)
        board_add_btn.click()
        
        return BoardPage(self.driver)
    


