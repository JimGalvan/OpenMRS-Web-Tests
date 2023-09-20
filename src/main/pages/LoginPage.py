import logging

from selenium.webdriver.common.by import By

from src.main.pages.BasePage import BasePage
from src.main.utils.logger import logger


class LoginPage(BasePage):
    """Page class for login functionality."""

    def __init__(self, driver):
        """
        Initializes a new instance of the LoginPage.

        Args:
            driver (WebDriver): The WebDriver instance.
        """
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.XPATH, "//*[text()='Log in']")
        self.continue_button = (By.XPATH, "//*[text()='Continue']")
        self.confirm_button = (By.XPATH, "//button[@type='submit']//span")

    def open(self):
        """Open the login page."""
        logger.info("Opening the login page")
        self.driver.get("https://o3.openmrs.org/openmrs/spa/login")

    def login(self, username, password):
        """
        Perform login action with provided username and password.

        Args:
            username (str): The username to log in with.
            password (str): The password to log in with.
        """
        logger.info("Logging in with username: %s", username)
        self.set_text(self.username_input, username)
        self.click(self.continue_button)
        self.set_text(self.password_input, password)
        self.click(self.login_button)

    def select_location(self, location):
        """
        Select a specific location.

        Args:
             location (str): The location to select.
        """
        logger.info("Selecting location: %s", location)
        location_selector = (
            By.XPATH,
            "//label[@for='<location>']//span[contains(@class,'radio')]".replace("<location>", location.strip()))
        self.click(location_selector)
        self.click(self.confirm_button)
