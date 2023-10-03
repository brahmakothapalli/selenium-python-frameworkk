from utils import logger_config
from helpers.waits_helper import WaitsHelper
from selenium.webdriver.remote.webdriver import WebDriver


class ElementsHelper:
    """ this class contains common action methods on webelements"""

    --logger = logger_config.get_logger()

    @staticmethod
    def find(driver: WebDriver, locator):
        WaitsHelper.wait_for_element_visibility(driver, locator)
        return driver.find_element(*locator)

    @staticmethod
    def click_element(driver: WebDriver, locator):
        ElementsHelper.find(driver, locator).click()

    @staticmethod
    def is_element_displayed(driver: WebDriver, locator):
        return ElementsHelper.find(driver, locator).is_displayed()

    @staticmethod
    def is_element_exist(driver: WebDriver, locator):
        return len(driver.find_elements(*locator)) != 0
