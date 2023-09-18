from selenium.webdriver.common.by import By

from src.main.pages.BasePage import BasePage


class PatientSummaryDashboardPage(BasePage):
    def __init__(self, driver):
        """
        Initializes a new instance of the PatientRegistrationPage.

        Args:
            driver (WebDriver): The WebDriver instance.
        """
