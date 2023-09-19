import time

from selenium.common import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.main.utils.logger import logger


class BasePage:
    timeout = 30
    short_timeout = 6
    max_attempts = 2

    def __init__(self, driver):
        """
        Initialize BasePage with a WebDriver instance.

        Args:
            driver (WebDriver): WebDriver instance from Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, self.timeout)

    def wait_for_visibility_of_element(self, locator, custom_timeout=30):
        """
        Wait for an element to be visible on the page.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).
            custom_timeout (int): The maximum time to wait for the element to be visible, in seconds. Default is 10 seconds.

        Returns:
            WebElement: The WebDriver element once it is visible.
        """
        return WebDriverWait(self.driver, custom_timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_presence_of_element(self, locator):
        """
        Wait for an element to be present in the DOM.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).

        Returns:
            WebElement: The WebDriver element once it is present in the DOM.
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_clickable(self, locator):
        """
        Wait for an element to be clickable.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).

        Returns:
            WebElement: The WebDriver element once it is clickable.
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """
        Click on an element.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).
        """
        element = self.scroll_to_element(locator)
        element.click()

    def set_text(self, locator, text):
        """
        Set text in an input field.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).
            text (str): The text to be entered into the input field.
        """

        attempt = 1

        while attempt <= self.max_attempts:

            element = self.wait_for_clickable(locator)

            try:
                element.click()
            except Exception as e:
                logger.exception(e)

            try:
                element.clear()
                element.send_keys(text)
                break
            except Exception as e:
                logger.exception(e)
                time.sleep(self.short_timeout)

            attempt += 1

    def get_text(self, locator):
        """
        Get the text of an element.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).

        Returns:
            str: The text of the element.
        """
        element = self.wait_for_visibility_of_element(locator)
        return element.text

    def get_attribute(self, locator, attribute):
        """
        Get the value of a specified attribute of an element.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).
            attribute (str): The attribute name.

        Returns:
            str: The value of the specified attribute.
        """
        element = self.wait_for_visibility_of_element(locator)
        return element.get_attribute(attribute)

    def is_displayed(self, locator):
        """
        Check if an element is displayed on the page.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).

        Returns:
            bool: True if the element is displayed, False otherwise.
        """
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def is_enabled(self, locator):
        """
        Check if an element is enabled.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).

        Returns:
            bool: True if the element is enabled, False otherwise.
        """
        element = self.wait_for_visibility_of_element(locator)
        return element.is_enabled()

    def is_selected(self, locator):
        """
        Check if a checkbox or radio button is selected.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).

        Returns:
            bool: True if the element is selected, False otherwise.
        """
        element = self.wait_for_visibility_of_element(locator)
        return element.is_selected()

    def click_with_js(self, locator):
        """
        Click an element using JavaScript.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).
            :param locator:
            :param self:
        """
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        """
        Scroll to a specific element on the page using JavaScript and wait for its visibility.

        Args:
            locator (tuple): A tuple representing the locator strategy and value (e.g., (By.ID, 'element_id')).
        """

        element = self.wait_for_visibility_of_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    def scroll_down_quarter_page(self):
        """
        Scroll down a quarter of the page using JavaScript.

        This function scrolls down by a quarter of the page's height using JavaScript.

        Returns:
            None
        """
        try:
            # Initialize the webdriver
            driver = self.driver

            # Calculate the number of pixels to scroll (a quarter of the page height)
            viewport_height = driver.execute_script("return window.innerHeight")
            quarter_scroll = viewport_height // 4

            # Scroll down by the calculated amount
            driver.execute_script(f"window.scrollBy(0, {quarter_scroll})")

            logger.info("Scrolled down a quarter of the page.")

        except Exception as e:
            logger.exception("An error occurred while scrolling down the page: %s", str(e))
            pass

    def scroll_to_bottom(self):
        """
        Scroll to the bottom of a web page using Selenium.

        Returns:
            None
        """
        try:
            # Scroll down to the bottom of the page
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            logger.info("Scrolled to the bottom of the page.")

        except Exception as e:
            logger.exception("An error occurred while scrolling to the bottom: {}".format(str(e)))

    def scroll_to_top(self):
        """
        Scrolls to the top of a web page using Selenium.

        Returns:
            None
        """
        try:
            # Scroll to the top of the page
            self.driver.execute_script("window.scrollTo(0, 0);")

            logger.info("Scrolled to the top of the page.")
        except Exception as e:
            logger.error(f"An error occurred while scrolling to the top: {str(e)}")
