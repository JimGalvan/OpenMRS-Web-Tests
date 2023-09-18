import pytest
from faker import Faker


@pytest.fixture(scope="module")
def patient_data():
    fake = Faker()
    first_name = fake.first_name()
    middle_name = fake.first_name()  # Adding middle name
    last_name = fake.last_name()
    family_name = "Test"
    dob_datetime = fake.date_of_birth(minimum_age=18, maximum_age=90)
    dob = dob_datetime.strftime("%d/%m/%Y")  # Format dob to "dd/mm/YYYY"
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address()
    gender = fake.random_element(elements=('Male', 'Female'))  # Adding gender
    country = fake.country()  # Adding country
    state_province = fake.state()  # Adding state/province
    county_district = fake.state()  # Adding county/district

    return {
        'location': "Outpatient Clinic",  # temp hardcoded
        'first_name': first_name,
        'middle_name': middle_name,
        'last_name': last_name,
        'family_name': family_name,
        'dob': dob,
        'email': email,
        'phone_number': phone_number,
        'address': address,
        'gender': gender,
        'country': country,
        'state_province': state_province,
        'county_district': county_district
    }
