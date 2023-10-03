from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoAlertPresentException
from utils import logger_config


class AlertsHelper:
    """ alerts helper class"""
    __logger = logger_config.get_logger()

    @staticmethod
    def is_alert_present(driver: WebDriver):
        try:
            driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    @staticmethod
    def accept_alert_without_text(driver: WebDriver):
        try:
            alert = driver.switch_to.alert
            alert.accept()
        except Exception as e:
            AlertsHelper.__logger.error(f"failed to accept the alert - {e}")
            raise e

    @staticmethod
    def accept_alert_with_text(driver: WebDriver, text):
        try:
            alert = driver.switch_to.alert
            alert.send_keys(text)
            alert.accept()
        except Exception as e:
            AlertsHelper.__logger.error(f"failed to accept the alert - {e}")
            raise e

    @staticmethod
    def dismiss_alert(driver: WebDriver):
        try:
            alert = driver.switch_to.alert
            alert.dismiss()
        except Exception as e:
            AlertsHelper.__logger.error(f"failed to dismiss the alert - {e}")
            raise e

    @staticmethod
    def get_alert_text(driver: WebDriver):
        try:
            return driver.switch_to.alert.text
        except Exception as e:
            AlertsHelper.__logger.error(f"failed to get the alert text - {e}")
            raise e
