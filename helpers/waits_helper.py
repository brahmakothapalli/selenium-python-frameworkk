from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import NoSuchElementException

from utils import read_configuration


class WaitsHelper:
    """ waits helper class"""

    @staticmethod
    def dynamic_wait(driver):
        return WebDriverWait(driver, read_configuration.get_timeperiod(), poll_frequency=read_configuration.get_polling_frequency(), ignored_exceptions=[NoSuchElementException])

    @staticmethod
    def wait_for_element_visibility(driver: WebDriver, locator):
        wait = WaitsHelper.dynamic_wait(driver)
        wait.until(EC.visibility_of_element_located(locator))

    @staticmethod
    def wait_for_element_invisibility(driver: WebDriver, locator):
        wait = WaitsHelper.dynamic_wait(driver)
        wait.until(EC.invisibility_of_element(locator))


def wait_for_element_clickable(driver: WebDriver, locator):
    wait = WaitsHelper.dynamic_wait(driver)
    wait.until(EC.element_to_be_clickable(locator))
