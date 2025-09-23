import os

# Environment variable names
BROWSER = "BROWSER"
SCREEN_WIDTH = "SCREEN_WIDTH"
SCREEN_HEIGHT = "SCREEN_HEIGHT"
HEADLESS = "HEADLESS"
WEKAN_URL = "WEKAN_URL"
TEST_NAME = "TEST_NAME"
ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"

# Default values
DEFAULT_BROWSER = "chrome"
DEFAULT_SCREEN_WIDTH = "1920"
DEFAULT_SCREEN_HEIGHT = "1080"
DEFAULT_HEADLESS = "false"
DEFAULT_WEKAN_URL = "http://localhost"
DEFAULT_TEST_NAME = "default_test_name"
class Config:
    BASE_URL = os.environ.get(WEKAN_URL, DEFAULT_WEKAN_URL)
    LOGIN_PATH = '/sign-in'
    LOGIN_PATH_TEXT = 'sign-in'
    TEST_USERNAME = 'testUsername'
    TEST_PASSWORD = 'testPassword'
    VALID_USERNAME = 'omriza5@gmail.com'
    VALID_PASSWORD = '123456'
    LOGIN_ERROR_MESSAGE = 'Login forbidden'
    
    @classmethod
    def browser(cls):
        return os.getenv(BROWSER, DEFAULT_BROWSER)
    
    @classmethod
    def screen_width(cls):
        return int(os.getenv(SCREEN_WIDTH, DEFAULT_SCREEN_WIDTH))

    @classmethod
    def screen_height(cls):
        return int(os.getenv(SCREEN_HEIGHT, DEFAULT_SCREEN_HEIGHT))

    @classmethod
    def headless(cls):
        return os.getenv(HEADLESS, DEFAULT_HEADLESS).lower() == 'true'

    @classmethod
    def wekan_url(cls):
        return os.getenv(WEKAN_URL, DEFAULT_WEKAN_URL)

    @classmethod
    def get_anthropic_api_key(cls):
        return os.getenv(ANTHROPIC_API_KEY, None)
    
    @classmethod
    def get_home_url(cls):
        return f"{cls.BASE_URL}"
    
    @classmethod
    def get_login_url(cls):
        return f"{cls.BASE_URL}{cls.LOGIN_PATH}"