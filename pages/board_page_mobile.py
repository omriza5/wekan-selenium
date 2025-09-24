from pages.base.board_page_base import BoardPageBase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BoardPageMobile(BoardPageBase):
    """
    Mobile implementation of BoardPage.
    Overrides mobile-specific behaviors.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.chevron_icon = (By.CSS_SELECTOR, ".fa-angle-right")
        self.wait = WebDriverWait(self.driver, 10)
    
    def _prepare_list_for_card_addition(self, list_element):
        """
        Mobile-specific preparation: click chevron icon to expand list options.
        """
        try:
            chevron_icon = self.wait.until(
                EC.element_to_be_clickable(
                    list_element.find_element(*self.chevron_icon)
                )
            )
            chevron_icon.click()
        except Exception as e:
            # Log the error but don't fail the test - maybe the list is already expanded
            print(f"Warning: Could not click chevron icon: {str(e)}")