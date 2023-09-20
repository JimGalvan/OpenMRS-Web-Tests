from selenium.webdriver.common.by import By
from src.main.pages.BasePage import BasePage
from src.main.utils.logger import logger
from src.main.utils.PropertiesReader import get_config_properties


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_patient_button = (By.XPATH, "//button[@name='AddPatientIcon']")

    def open(self):
        """Open the login page."""
        logger.info("Opening the home page")

        base_url = get_config_properties().get_value("base_url")

        self.driver.get(f"{base_url}/openmrs/spa/home")

    def click_add_patient_button(self):
        self.click(self.add_patient_button)

