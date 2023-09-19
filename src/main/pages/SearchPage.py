import time
import logging
from selenium.webdriver.common.by import By
from src.main.pages.BasePage import BasePage
from src.main.utils.logger import logger


class SearchPage(BasePage):
    """
    Page object for the search page.
    """

    def __init__(self, driver):
        """
        Initialize SearchPage instance.

        Args:
            driver: WebDriver instance.
        """
        super().__init__(driver)
        self.results_container = (By.XPATH, "//div[contains(@class,'patientSearchResultsDesktop')]")

    def get_search_results_text(self):
        """
        Get the search results text.

        Returns:
            str: The search results text.
        """
        results = self.get_text(self.results_container)

        max_attempts = 5
        attempt = 1

        while "Searching..." in results and attempt <= max_attempts:
            results = self.get_text(self.results_container)
            time.sleep(1)
            attempt += 1

        logger.info("Search results: %s", results)
        return results

    def click_patient(self, patient_full_name):
        self.click((By.XPATH, "//span[text()='{patient_name}']".replace("{patient_name}", patient_full_name)))
