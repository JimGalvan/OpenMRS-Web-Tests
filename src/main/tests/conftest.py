import pytest
from selenium import webdriver
from jproperties import Properties
import src.main.utils.file_utils as file_utils
from src.main.utils.logger import logger


class InvalidBrowser(Exception):
    pass


@pytest.fixture
def test_user():
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
    configs = Properties()
    config_file_path = file_utils.get_config_path()

    with open(config_file_path, 'rb') as read_prop:
        configs.load(read_prop)

    browser = str(configs.get("browser").data).strip().lower()

    # Initialize WebDriver based on the browser specified
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
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
