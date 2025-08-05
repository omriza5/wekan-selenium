from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.header_main_bar = (By.ID, "header-main-bar")
        self.username = "omriza5@gmail.com"
        self.password = "123456"

    def open_page(self):
        """
        This method checks if the home page is healthy by verifying the title.
        """
        login_page = LoginPage(self.driver)
        login_page.login(self.username, self.password)
    
    def is_header_displayed(self):
        """
        This method checks if the header is displayed on the home page.
        """
        header_element = self.driver.find_element(*self.header_main_bar)
        return header_element.is_displayed()
