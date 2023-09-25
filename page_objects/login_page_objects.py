from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from base.BasePage import BasePage


class LoginPageObjects(BasePage):
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "submit")
    __login_success_text = (By.TAG_NAME, "h1")
    __logout_button = (By.LINK_TEXT, 'Log out')
    __login_error_text = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__int__(driver)

    def enter_user_credentials(self, user_name, password):
        self.enter_text(self.__username_field, user_name)
        self.enter_text(self.__password_field, password)

    def click_submit_button(self):
        self.click(self.__submit_button)

    def get_login_success_text(self) -> str:
        self.take_screen_shot()
        return self.get_text(self.__login_success_text)

    @property
    def get_current_url(self) -> str:
        return self.driver.current_url

    def is_logout_button_displayed(self) -> bool:
        return self.is_element_displayed(self.__logout_button)

    def get_error_text(self) -> str:
        return self.get_text(self.__login_error_text)
