import time

from src.main.pages.Header import Header
from src.main.pages.HomePage import HomePage
from src.main.pages.LoginPage import LoginPage
from src.main.pages.PatientProfilePage import PatientProfilePage
from src.main.pages.PatientRegistrationPage import PatientRegistrationPage
from src.main.fixtures.patient_test_data import patient_data
from src.main.pages.PatientSummaryDashboardPage import PatientSummaryDashboardPage
from src.main.pages.SearchPage import SearchPage
from src.main.pages.ToastNotification import ToastNotification
import src.main.utils.logger as logger
from src.main.fixtures.expected_ui_text import expected_messages


def test_add_patient(driver, patient_data, expected_messages, admin_user):
    """
       Test case to verify the functionality of adding a new patient.
       Author: Jim Galvan
    """

    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    patient_registration_page = PatientRegistrationPage(driver)
    toast_notification = ToastNotification(driver)

    login_page.open()
    login_page.login(admin_user["username"], admin_user["password"])
    login_page.select_location(patient_data["location"])

    home_page.click_add_patient_button()

    # Fill info from the bottom to the top to avoid input loading issues

    patient_registration_page.register_patient(
        patient_data['first_name'],
        patient_data['middle_name'],
        patient_data['family_name'],
        "Male",
        patient_data['dob'],
        patient_data['phone_number'],
        patient_data['state_province'],
        patient_data['county_district'],
        patient_data['country']
    )

    assert expected_messages[
               "PATIENT_REGISTERED_SUCCESSFULLY_MSG_TITLE"] in toast_notification.get_toast_message(timeout=30)
    assert expected_messages["PATIENT_REGISTERED_SUCCESSFULLY_MSG"] in toast_notification.get_toast_message(timeout=30)


def test_patient_search_and_view(driver, patient_data, expected_messages, admin_user):
    """
        Test case to verify the functionality of patient search and view.
        Author: Jim Galvan
    """

    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    patient_registration_page = PatientRegistrationPage(driver)
    toast_notification = ToastNotification(driver)
    header = Header(driver)
    search_page = SearchPage(driver)
    patient_profile_page = PatientProfilePage(driver)

    login_page.open()
    login_page.login(admin_user["username"], admin_user["password"])
    login_page.select_location(patient_data["location"])

    home_page.click_add_patient_button()

    # Fill info from the bottom to the top to avoid input loading issues

    patient_registration_page.register_patient(
        patient_data['first_name'],
        patient_data['middle_name'],
        patient_data['family_name'],
        "Male",
        patient_data['dob'],
        patient_data['phone_number'],
        patient_data['state_province'],
        patient_data['county_district'],
        patient_data['country']
    )

    toast_notification.wait_for_toast_message_to_be_visible()

    home_page.open()

    patient_full_name = patient_data['first_name'] + " " + patient_data['middle_name'] + " " + patient_data[
        'family_name']

    header.set_search_input_text(patient_full_name)

    time.sleep(3)

    assert patient_full_name in header.get_search_results_text()

    header.click_search_button()

    assert patient_full_name in search_page.get_search_results_text()

    search_page.click_patient(patient_full_name)

    assert patient_profile_page.is_patient_full_name_displayed(patient_full_name) is True
