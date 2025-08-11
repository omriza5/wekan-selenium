import time
from selenium.webdriver.common.by import By
from utils.screenshot import take_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoardPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.add_list_button = (By.XPATH, "//div[@class='list-header-add']/a[contains(@class, 'open-list-composer') and contains(@class, 'js-open-inlined-form') and @title='Add List']")
        self.list_title_textbox = (By.CSS_SELECTOR, "input.list-name-input.full-line")
        self.save_list_button = (By.CSS_SELECTOR, "button.primary.confirm[type='submit']")
        self.close_list_dialog_button = (By.CSS_SELECTOR, ".fa-times-thin")
        self.list_name_elements = (By.CSS_SELECTOR, ".list-header-name .viewer p")
        self.add_card_to_top_button = (By.CSS_SELECTOR, "a.js-add-card.list-header-plus-top[title='Add Card to Top of List']")
        self.add_card_to_bottom_button = (By.CSS_SELECTOR, "a.open-minicard-composer.js-card-composer.js-open-inlined-form[title='Add Card to Bottom of List']")
        self.save_card_button = (By.CSS_SELECTOR, "div.add-controls button.primary.confirm[type='submit']")
        self.card_title_textbox = (By.CSS_SELECTOR, "textarea.minicard-composer-textarea.js-card-title")

    def add_list(self, list_name):
        """
        This method adds a new list to the board.
        """
        take_screenshot(self.driver, "before_add_list")
        wait = WebDriverWait(self.driver, 20)
        add_list_btn = wait.until(EC.element_to_be_clickable(self.add_list_button))
        take_screenshot(self.driver, "after waiting for add_list_btn")
        add_list_btn.click()
        take_screenshot(self.driver, "after_click_add_list")
        list_title = self.driver.find_element(*self.list_title_textbox)
        list_title.send_keys(list_name)
        save_btn = self.driver.find_element(*self.save_list_button)
        save_btn.click()
        close_dialog_btn = self.driver.find_element(*self.close_list_dialog_button)
        close_dialog_btn.click()
        
        return self
    
    def get_list_names(self):
        elements = self.driver.find_elements(*self.list_name_elements)
        return [el.text.strip() for el in elements]
    
    def add_card_to_bottom(self, list_name, card_title):
        """
        This method adds a card to the bottom of a specified list.
        """
        lists = self.get_list_names()
        if list_name not in lists:
            raise ValueError(f"List '{list_name}' not found on the board.")
        
        # Find the list and click the button to add a card
        list_selector = self.get_list_selector(list_name)
        list_element = self.driver.find_element(*list_selector)
        add_card_btn = list_element.find_element(*self.add_card_to_bottom_button)
        add_card_btn.click()
        
        # Enter the card title and save
        card_title_input = list_element.find_element(*self.card_title_textbox)
        card_title_input.send_keys(card_title)
        save_card_btn = list_element.find_element(*self.save_card_button)
        save_card_btn.click()
        
        return self
        
        
    def get_list_selector(self, list_name):
        """
        Dynamically generates a selector for the parent list div based on its name.
        """
        return (By.XPATH, f"//div[contains(@class, 'list js-list') and .//p[text()='{list_name}']]")

    def get_list_cards_titles(self, list_name):
        """
        Retrieves the titles of all cards in a specified list.
        """
        # Get the dynamic selector for the parent list div
        list_selector = self.get_list_selector(list_name)
        
        # Find the list element
        list_element = self.driver.find_element(*list_selector)
        
        # Locate all cards within the list
        card_elements = list_element.find_elements(By.CSS_SELECTOR, ".minicard .minicard-title")
        
        # Extract and return the text of each card
        return [card.text.strip() for card in card_elements]

