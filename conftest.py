import pytest
import allure
from utils.config import Config


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    suite_name = Config.suite_name()
    browser = Config.browser()
    resolution = f"{Config.screen_width()}x{Config.screen_height()}"
    if suite_name:
        allure.dynamic.suite(suite_name)
    if browser and resolution:
        allure.dynamic.label("browser", browser)
        allure.dynamic.label("resolution", resolution)