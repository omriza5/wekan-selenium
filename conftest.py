import os
import pytest
import allure

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    suite_name = os.getenv("ALLURE_SUITE")
    if suite_name:
        allure.dynamic.suite(suite_name)