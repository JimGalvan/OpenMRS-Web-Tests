import time

from src.main.pages.HomePage import HomePage
from src.main.pages.LoginPage import LoginPage
from src.main.pages.PatientRegistrationPage import PatientRegistrationPage
from src.main.fixtures.patient_test_data import patient_data
from src.main.pages.PatientSummaryDashboardPage import PatientSummaryDashboardPage
from src.main.pages.ToastNotification import ToastNotification
from src.main.utils.logger import logger
from src.main.fixtures.expected_ui_text import expected_messages


def test_add_patient(driver, patient_data, expected_messages, test_user):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    patient_registration_page = PatientRegistrationPage(driver)
    toast_notification = ToastNotification(driver)

    login_page.open()
    login_page.login(test_user["username"], test_user["password"])
    login_page.select_location(patient_data["location"])

    home_page.click_add_patient_button()

    # Fill info from the bottom to the top to avoid input loading issues

    patient_registration_page.scroll_to_bottom()
    patient_registration_page.set_phone(patient_data['phone_number'])
    patient_registration_page.set_state_province(patient_data['state_province'])
    patient_registration_page.set_county_district(patient_data['county_district'])
    patient_registration_page.set_country(patient_data['country'])

    patient_registration_page.scroll_to_top()
    patient_registration_page.set_first_name(patient_data['first_name'])
    patient_registration_page.set_middle_name(patient_data['middle_name'])
    patient_registration_page.set_family_name(patient_data['family_name'])
    patient_registration_page.select_sex("Male")
    patient_registration_page.set_birthdate(patient_data['dob'])

    patient_registration_page.click_register_patient_button()

    assert expected_messages[
               "PATIENT_REGISTERED_SUCCESSFULLY_MSG_TITLE"] in toast_notification.get_toast_message(timeout=30)
    assert expected_messages["PATIENT_REGISTERED_SUCCESSFULLY_MSG"] in toast_notification.get_toast_message(timeout=30)
