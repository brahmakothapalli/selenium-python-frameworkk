from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

from base.BasePage import BasePage


class DashboardPageObjects(BasePage):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__int__(driver)

    __logout_button = (By.LINK_TEXT, 'Log out')

    def is_logout_button_displayed(self) -> bool:
        return self.is_element_displayed(self.__logout_button)
