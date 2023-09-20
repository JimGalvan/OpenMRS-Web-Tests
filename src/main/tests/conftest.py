import pytest
from selenium import webdriver
from src.main.utils.PropertiesReader import get_config_properties
from src.main.utils.logger import logger
from os import path
from selenium.webdriver.firefox.service import Service


@pytest.fixture
def admin_user():
    """
    Fixture to provide test user information.
    """
    return {"username": "admin", "password": "Admin123"}


@pytest.fixture(scope="module")
def driver():
    """
    Fixture to set up the WebDriver based on browser configuration.
    """

    # Load browser configuration from properties
    properties_reader = get_config_properties()
    properties_reader.get_value("browser")

    browser = properties_reader.get_value("browser")

    # setup service to disable firefox log
    service = Service(log_path=path.devnull)

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        logger.error(f"Invalid browser: {browser}. Using default browser chrome")
        driver = webdriver.Chrome()

    driver.maximize_window()
    return driver


@pytest.fixture(autouse=True)
def run_around_tests():
    """
    Fixture to set up and tear down resources before and after each test.
    """
    # Set up resources or perform other tasks before the test is run
    yield
    # Tear down resources or perform other tasks after the test is run
