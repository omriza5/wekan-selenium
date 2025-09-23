from selenium.webdriver.common.by import By
from utils.dom_xpath_locator import DOMXPathLocator
from utils.config import Config

class HomeBase: 
    def __init__(self, driver):
        self.driver = driver
        self.locator = DOMXPathLocator(driver, Config.get_home_url())
    
    def find_element_by_description(self, element_description):
        try:
            return self.locator.find_element_by_xpath(element_description)
        except Exception as e:
            raise Exception(f"Error finding element by description '{element_description}': {str(e)}")
        
    def create_new_board(self):
        try:
            element_description = "add-board card"
            card = self.find_element_by_description(element_description)
            card.click()
        except Exception as e:
            raise Exception(f"Error opening app dropdown menu: {str(e)}")