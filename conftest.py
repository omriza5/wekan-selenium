import pytest
import allure
from utils.config import Config

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    suite_name = Config.suite_name()
    browser = Config.browser()
    resolution = f"{Config.screen_width()}x{Config.screen_height()}"
    # Compose a unique suite name per matrix job
    if suite_name and browser and resolution:
        allure.dynamic.suite(f"{suite_name} [{browser} {resolution}]")
    elif browser and resolution:
        allure.dynamic.suite(f"{browser} {resolution}")
    elif suite_name:
        allure.dynamic.suite(suite_name)