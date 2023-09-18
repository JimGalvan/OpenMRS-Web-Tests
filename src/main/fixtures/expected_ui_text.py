import pytest


@pytest.fixture(scope="module")
def expected_messages():
    return {
        'PATIENT_REGISTERED_SUCCESSFULLY_MSG_TITLE': 'New Patient Created',
        'PATIENT_REGISTERED_SUCCESSFULLY_MSG': 'The patient can now be found by searching for them using their name or'
                                               ' ID number'
    }
