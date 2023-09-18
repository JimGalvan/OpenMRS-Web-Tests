from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from src.main.pages.BasePage import BasePage
from src.main.utils.logger import logger


class PatientRegistrationPage(BasePage):
    """Page class for patient registration."""

    def __init__(self, driver):
        """
        Initializes a new instance of the PatientRegistrationPage.

        Args:
            driver (WebDriver): The WebDriver instance.
        """
        super().__init__(driver)

        # Locators
        self.first_name_input = (By.ID, "givenName")
        self.middle_name_input = (By.ID, "middleName")
        self.family_name_input = (By.ID, "familyName")
        self.gender_input = (By.NAME, "gender")  # Assuming gender is a name attribute
        self.birthdate_input = (By.ID, "birthdate")
        self.country_input = (By.ID, "country")
        self.state_province_input = (By.ID, "stateProvince")
        self.county_district_input = (By.ID, "countyDistrict")
        self.phone_input = (By.ID, "phone")
        self.submit_button = (By.XPATH, "//button[@type='submit']")

    def set_first_name(self, value):
        """
        Sets the given name input.

        Args:
            value (str): The value to set in the input field.
        """
        logger.info("Setting given name to: %s", value)
        self.set_text(self.first_name_input, value)

    def set_middle_name(self, value):
        """
        Sets the middle name input.

        Args:
            value (str): The value to set in the input field.
        """
        logger.info("Setting middle name to: %s", value)
        self.set_text(self.middle_name_input, value)

    def set_family_name(self, value):
        """
        Sets the family name input.

        Args:
            value (str): The value to set in the input field.
        """
        logger.info("Setting family name to: %s", value)
        self.set_text(self.family_name_input, value)

    # Continue with similar doc comments and logging for other functions...

    def set_phone(self, value):
        """
        Sets the phone input.

        Args:
            value (str): The value to set in the input field.
        """
        logger.info("Setting phone to: %s", value)
        self.set_text(self.phone_input, value)

    def set_gender(self, value):
        """
        Sets the gender input.

        Args:
            value (str): The value to set for gender.
        """
        logger.info("Setting gender to: %s", value)
        # Add your code to set the gender

    def set_birthdate(self, value):
        """
        Sets the birthdate input.

        Args:
            value (str): The value to set in the input field.
        """
        logger.info("Setting birthdate to: %s", value)
        self.set_text(self.birthdate_input, value)

    def set_country(self, value):
        """
        Sets the country input.

        Args:
            value (str): The value to set in the input field.
        """
        logger.info("Setting country to: %s", value)
        self.set_text(self.country_input, value)

    def set_state_province(self, value):
        """
        Sets the state/province input.

        Args:
            value (str): The value to set in the input field.
        """
        logger.info("Setting state/province to: %s", value)
        self.set_text(self.state_province_input, value)

    def set_county_district(self, value):
        """
        Sets the county/district input.

        Args:
            value (str): The value to set in the input field.
        """
        logger.info("Setting county/district to: %s", value)
        self.set_text(self.county_district_input, value)

    def select_sex(self, sex):
        """
        Selects the radio button corresponding to the specified sex.

        Args:
            sex (str): The sex to be selected ('male' or 'female').

        Returns:
            None
        """
        radio_locator = (
            By.XPATH, "//*[@for='<sex>']//span[contains(@class,'radio')]".replace("<sex>", sex.lower()))
        self.click(radio_locator)

    def click_register_patient_button(self):
        """
        Clicks the Register Patient button.

        This method logs the action of clicking the Register Patient button
        and then clicks the button using the 'click' method.

        Args:
            None

        Returns:
            None
        """
        logger.info("Clicking Register Patient button")
        self.click(self.submit_button)

    def click_to_hide_calendar(self):
       self.click_with_js(self.country_input)