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
        self.add_board_btn = (By.CSS_SELECTOR, "input.primary.wide[type='submit'][value='Create']")
    
    def is_header_displayed(self):
        """
        This method checks if the header is displayed on the home page.
        """
        header_element = self.driver.find_element(*self.header_main_bar)
        return header_element.is_displayed()
    
    def create_board(self, board_title):
        # Find and click the "Add Board" link
        borad_link = self.driver.find_element(*self.add_board_link)
        borad_link.click()
        
        # Find and fill the board title field
        board_title_field = self.driver.find_element(*self.board_title_textbox)
        board_title_field.clear()
        board_title_field.send_keys(board_title)
        
        # Explicitly wait for the "Create" button to be clickable
        wait = WebDriverWait(self.driver, 50)  # Wait up to 10 seconds
        board_add_btn = wait.until(EC.presence_of_element_located(self.add_board_btn))
        board_add_btn.click()
        
        return BoardPage(self.driver)
