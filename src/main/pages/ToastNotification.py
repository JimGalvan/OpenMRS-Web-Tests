from src.main.pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ToastNotification(BasePage):
    def __init__(self, driver):
        """
        Initializes a new instance of the PatientRegistrationPage.

        Args:
            driver (WebDriver): The WebDriver instance.
        """
        super().__init__(driver)
        self.toast_message_text = (By.XPATH, "//*[@role='status' and contains(@class, 'cds--toast-notification')]")

    def get_toast_message(self, timeout=20):
        self.wait_for_visibility_of_element(self.toast_message_text, timeout)
        return self.get_text(self.toast_message_text)
