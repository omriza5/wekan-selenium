import os
from selenium.webdriver.chrome.options import Options

def get_chrome_options():
    options = Options()
    
    # Check if running in a CI environment (GitHub Actions sets GITHUB_ACTIONS=true)
    if os.getenv("GITHUB_ACTIONS") == "true" or os.getenv("HEADLESS") == "true":
        options.add_argument("--headless")  # Run in headless mode
        options.add_argument("--no-sandbox")  # Required for CI environments
        options.add_argument("--disable-dev-shm-usage")  # Prevent shared memory issues
        options.add_argument("--window-size=1920,1080")
    else:
        # Local development settings
        options.add_argument("--start-maximized")  # Start browser maximized
    
    return options