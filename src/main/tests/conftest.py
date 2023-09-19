import time

import pytest
from selenium import webdriver


@pytest.fixture
def test_user():
    return {"username": "admin", "password": "Admin123"}


# WebDriver setup
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    return driver


@pytest.fixture(autouse=True)
def run_around_tests():
    # Set up resources or perform other tasks before the test is run
    yield
    # Tear down resources or perform other tasks after the test is run
