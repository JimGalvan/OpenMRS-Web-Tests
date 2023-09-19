from selenium.webdriver.common.by import By

from src.main.pages.BasePage import BasePage


class PatientProfilePage(BasePage):
    def __init__(self, driver):
        """
        Initializes a new instance of the PatientProfilePage.

        Args:
            driver (WebDriver): The WebDriver instance.
        """
        super().__init__(driver)
        self.patient_header_banner = (By.XPATH, "//*[@data-extension-id='patient-banner']")

    def is_patient_full_name_displayed(self, patient_full_name):
        banner_text = self.get_text(self.patient_header_banner)
        return patient_full_name in banner_text

