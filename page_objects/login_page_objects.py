from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from base.BasePage import BasePage
from page_objects.dashboard_page_objects import DashboardPageObjects

from utils import logger_config


class LoginPageObjects(BasePage):
    logger = logger_config.get_logger()
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "submit")
    __login_success_text = (By.TAG_NAME, "h1")
    __login_error_text = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__int__(driver)

    def enter_user_credentials(self, user_name, password):
        self.logger.info("entering user credentials")
        try:
            self.enter_text(self.__username_field, user_name)
            self.enter_text(self.__password_field, password)
        except Exception as e:
            self.logger.error("failed to enter the credentials :: enter_user_credentials", e)
            raise e

    def click_submit_button(self):
        self.logger.info("clicking on the submit button")
        self.click(self.__submit_button)
        dashboard_page = DashboardPageObjects(self.driver)
        return dashboard_page

    def get_login_success_text(self) -> str:
        self.logger.info("getting login success text")
        self.take_screen_shot()
        return self.get_text(self.__login_success_text)

    @property
    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_error_text(self) -> str:
        return self.get_text(self.__login_error_text)
