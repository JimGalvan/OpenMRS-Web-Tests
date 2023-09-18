# Automation Framework with Python, Selenium, Pytest, and Page Object Model

## Overview
This project is a showcase of my skills in Python, Selenium, Pytest, and Page Object Model (POM) by creating a robust automation framework. The provided `test_add_patient` test case demonstrates the seamless integration of these technologies to automate patient registration on a web application.

## OpenMRS: Open Source Medical Record System

OpenMRS is an open-source electronic medical record (EMR) platform, designed for efficient patient data management and healthcare delivery, especially in resource-constrained environments. Its modular architecture and global community support enable customization, interoperability, and adaptation to various healthcare settings.

## Test Case Description
The `test_add_patient` test case simulates the process of adding a patient to the application, following a structured approach using the Page Object Model to interact with web elements efficiently and apply the required actions.

**Steps:**
1. **Login and Navigation**: Navigate to the login page, authenticate the test user, and select a specific location.
   
2. **Patient Registration**: Click the "Add Patient" button on the home page and populate patient information, scrolling from the bottom to the top to mitigate input loading issues.
   
3. **Registration Confirmation**: Click the "Register Patient" button and wait for the backend to process the registration.

4. **Assertions**: Assert that the expected success messages are present in the toast message displayed on the patient summary dashboard.

## Technologies Utilized
- **Python**: Primary programming language for automation scripting.
- **Selenium**: Used for browser automation and interacting with web elements.
- **Pytest**: Testing framework for structuring and organizing test cases effectively.
- **Page Object Model (POM)**: Implemented for maintainable and scalable automation, enhancing code reusability and readability.

This project not only demonstrates the automation of the patient registration process but also encapsulates a robust automation framework, showcasing efficient use of Python, Selenium, Pytest, and the Page Object Model.

---
