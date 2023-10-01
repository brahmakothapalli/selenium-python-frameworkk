from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils import logger_config
from base.BasePage import BasePage


class DashboardPageObjects(BasePage):

    logger = logger_config.get_logger()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__int__(driver)

    __logout_button = (By.LINK_TEXT, 'Log out')

    def is_logout_button_displayed(self) -> bool:
        self.logger.info("checking logout button after login")
        return self.is_element_displayed(self.__logout_button)
