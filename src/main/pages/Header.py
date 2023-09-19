import logging
from selenium.webdriver.common.by import By
from src.main.pages.BasePage import BasePage
from src.main.utils.logger import logger


class Header(BasePage):
    """
    Page object for the header section.
    """

    def __init__(self, driver):
        """
        Initialize Header instance.

        Args:
            driver: WebDriver instance.
        """
        super().__init__(driver)
        self.search_icon = (By.XPATH, "//*[@data-testid='searchPatientIcon']")
        self.search_input = (By.XPATH, "//*[@data-testid='patientSearchBar']")
        self.results_container = (By.XPATH, "//*[@data-testid='floatingSearchResultsContainer']|//*[contains(@class,'searchResultsTabletOrOverlay')]")
        self.search_button = (By.XPATH, "//button[text()='Search']")

    def click_search_icon(self):
        """
        Clicks on the search icon.
        """
        self.click(self.search_icon)

    def set_search_input_text(self, text):
        """
        Sets the text in the search input field.

        Args:
            text (str): Text to set in the search input field.
        """
        self.click_search_icon()
        self.set_text(self.search_input, text)

    def get_search_results_text(self):
        """
        Gets the search results text.

        Returns:
            str: The search results text.
        """
        results = self.get_text(self.results_container)
        logger.info("Search results: %s", results)
        return results

    def click_search_button(self):
        """
        Clicks the search button.
        """
        self.click(self.search_button)
