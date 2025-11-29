from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    # Selectores
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _CONTINUE_BTN = (By.ID, "continue")
    _FINISH_BTN = (By.ID, "finish")
    _COMPLETE_MSG = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def fill_information(self, first_name, last_name, postal_code):
        self.driver.find_element(*self._FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self._LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self._POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self._CONTINUE_BTN).click()

    def finish_checkout(self):
        self.driver.find_element(*self._FINISH_BTN).click()

    def get_complete_message(self):
        return self.driver.find_element(*self._COMPLETE_MSG).text
