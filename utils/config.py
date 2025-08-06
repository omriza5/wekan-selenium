import os

class Config:
    BASE_URL = os.environ.get('WEKAN_URL', 'http://localhost:80')
    LOGIN_PATH = '/sign-in'
    
    @classmethod
    def get_login_url(cls):
        return f"{cls.BASE_URL}{cls.LOGIN_PATH}"