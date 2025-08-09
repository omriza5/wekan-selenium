import os

class Config:
    BASE_URL = os.environ.get('WEKAN_URL', 'http://localhost:80')
    LOGIN_PATH = '/sign-in'
    LOGIN_PATH_TEXT = 'sign-in'
    TEST_USERNAME = 'testUsername'
    TEST_PASSWORD = 'testPassword'
    VALID_USERNAME = 'omriza5@gmail.com'
    VALID_PASSWORD = '123456'
    LOGIN_ERROR_MESSAGE = 'Login forbidden'
    
    @classmethod
    def get_login_url(cls):
        return f"{cls.BASE_URL}{cls.LOGIN_PATH}"