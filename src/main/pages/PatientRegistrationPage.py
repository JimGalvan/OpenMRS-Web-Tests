import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from src.main.pages.BasePage import BasePage
from src.main.pages.ToastNotification import ToastNotification
from src.main.utils.logger import logger


def set_gender(value):
    """
    Sets the gender input.

    Args:
        value (str): The value to set for gender.
    """
    logger.info("Setting gender to: %s", value)
    # Add your code to set the gender


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

    def register_patient(self, first_name, middle_name, family_name, sex, dob, phone_number, state_province,
                         county_district, country):
        """
        Fills the patient information in the application.

        Parameters:
        first_name (str): The first name of the patient.
        middle_name (str): The middle name of the patient.
        family_name (str): The family name or last name of the patient.
        sex (str): The gender of the patient (e.g., 'Male', 'Female', 'Other').
        dob (str): The date of birth of the patient in the format 'dd/mm/YYYY'.
        phone_number (str): The phone number of the patient.
        state_province (str): The state or province of the patient.
        county_district (str): The county or district of the patient.
        country (str): The country of the patient.

        This method scrolls to the bottom of the page and sets the provided phone number,
        state/province, county/district, and country. It then scrolls to the top of the page
        and sets the first name, middle name, family name, gender, and date of birth.
        """

        time.sleep(self.short_timeout)

        self.scroll_to_bottom()
        self.set_phone(phone_number)
        self.set_state_province(state_province)
        self.set_county_district(county_district)
        self.set_country(country)

        self.scroll_to_top()
        self.set_first_name(first_name)
        self.set_middle_name(middle_name)
        self.set_family_name(family_name)
        self.scroll_to_top()
        self.select_sex(sex)
        self.set_birthdate(dob)

        self.click_register_patient_button()

        toast_notification = ToastNotification(self.driver)

        # In Firefox sometimes the dob app validation fails, so the user needs to click twice.
        if "Incomplete form" in toast_notification.get_toast_message():
            self.click_register_patient_button()
