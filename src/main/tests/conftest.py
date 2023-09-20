import pytest
from selenium import webdriver
from jproperties import Properties
import src.main.utils.file_utils as file_utils
from src.main.utils.PropertiesReader import PropertiesReader
from src.main.utils.logger import logger
from os import path
from selenium.webdriver.firefox.service import Service


class InvalidBrowser(Exception):
    pass


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
    properties_reader = PropertiesReader("\\src\\resources\\config.properties")
    properties_reader.get_value("browser")

    browser = properties_reader.get_value("browser")

    # Initialize WebDriver based on the browser specified
    service = Service(log_path=path.devnull)

    if browser == "chrome":
        driver = webdriver.Chrome(service=service)
    elif browser == "firefox":
        driver = webdriver.Firefox(service=service)
    elif browser == "edge":
        driver = webdriver.Edge(service=service)
    else:
        logger.error(f"Invalid browser: {browser}")
        raise InvalidBrowser(f"Invalid browser: {browser}")

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
