import os

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator):
        self.wait_for_element_visibility(locator)
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def enter_text(self, locator, text):
        self.find(locator).send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_element_displayed(self, locator) -> bool:
        return self.find(locator).is_displayed()

    def wait_for_element_visibility(self, locator):
        wait = WebDriverWait(self.driver, 15)
        wait.until(ec.visibility_of_element_located(locator))

    def take_screen_shot(self):
        current_file_path = os.getcwd()
        current_working_path = os.path.dirname(current_file_path)
        self.driver.save_screenshot(current_working_path+"//reports//screenshot.png")
