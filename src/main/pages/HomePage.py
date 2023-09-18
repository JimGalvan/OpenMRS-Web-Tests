from selenium.webdriver.common.by import By

from src.main.pages.BasePage import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_patient_button = (By.XPATH, "//button[@name='AddPatientIcon']")

    def click_add_patient_button(self):
        self.click(self.add_patient_button)

