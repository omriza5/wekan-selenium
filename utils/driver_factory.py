from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config import Config

class DriverFactory:
    def __init__(self):
        self.browser = Config.browser()
        self.width = Config.screen_width()
        self.height = Config.screen_height()
        self.headless = Config.headless()

    def create_driver(self):
        if self.browser == 'chrome':
            return self._create_chrome_driver()
        elif self.browser == 'firefox':
            return self._create_firefox_driver()
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")
    
    def _create_chrome_driver(self):
        options = ChromeOptions()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument(f"--window-size={self.width},{self.height}")
        
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(self.width, self.height)
        return driver
    
    def _create_firefox_driver(self):
        options = FirefoxOptions()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument(f"--width={self.width}")
        options.add_argument(f"--height={self.height}")
        
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(self.width, self.height)
        options.binary_location = "/usr/local/bin/firefox"
        return driver

# Usage in your tests
def get_driver():
    factory = DriverFactory()
    return factory.create_driver()