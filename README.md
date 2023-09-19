# Automation Framework with Python, Selenium, Pytest, and Page Object Model

## Overview
This project is a showcase of my skills in Python, Selenium, Pytest, and Page Object Model (POM) by creating a robust automation framework. The provided test_add_patient and test_patient_search_and_view test cases demonstrate the seamless integration of these technologies to automate patient registration and patient search/view functionalities on a web application.

## Technologies Utilized
- **Python**: Primary programming language for automation scripting.
- **Selenium**: Used for browser automation and interacting with web elements.
- **Pytest**: Testing framework for structuring and organizing test cases effectively.
- **Page Object Model (POM)**: Implemented for maintainable and scalable automation, enhancing code reusability and readability.

This project not only demonstrates the automation of the patient registration process but also encapsulates a robust automation framework, showcasing efficient use of Python, Selenium, Pytest, and the Page Object Model.

## OpenMRS: Open Source Medical Record System

OpenMRS is an open-source electronic medical record (EMR) platform, designed for efficient patient data management and healthcare delivery, especially in resource-constrained environments. Its modular architecture and global community support enable customization, interoperability, and adaptation to various healthcare settings.

## Test Case 1 Description
The `test_add_patient` test case simulates the process of adding a patient to the application, following a structured approach using the Page Object Model to interact with web elements efficiently and apply the required actions.

**Steps:**
1. **Login and Navigation**: Navigate to the login page, authenticate the test user, and select a specific location.
   
2. **Patient Registration**: Click the "Add Patient" button on the home page and populate patient information, scrolling from the bottom to the top to mitigate input loading issues.
   
3. **Registration Confirmation**: Click the "Register Patient" button and wait for the backend to process the registration.

4. **Assertions**: Assert that the expected success messages are present in the toast message displayed on the patient summary dashboard.

## Test Case 2 Description

The `test_patient_search_and_view` test case focuses on the functionality of searching for a patient and viewing their profile within the application. This test case utilizes the Page Object Model approach for effective interaction with web elements and proper execution of actions.

**Steps:**

1. **Login and Navigation**: Navigate to the login page, authenticate the test user, and select a specific location.

2. **Patient Registration**: Click the "Add Patient" button on the home page and populate patient information, ensuring input from the bottom to the top to handle input loading issues.

3. **Registration Confirmation**: Click the "Register Patient" button and wait for the backend to process the registration. Confirm registration success with a toast notification.

4. **Search and Verify**: Return to the home page and perform a search using the patient's full name. Verify the patient's name in the search results.

5. **View Patient Profile**: Click on the patient's name in the search results to view the patient's profile. Verify the patient's full name is correctly displayed.

**Assertions:**
- Assert that the patient's full name is displayed in the search results after the search is performed.
- Assert that the patient's full name is correctly displayed on the patient profile page.

---
