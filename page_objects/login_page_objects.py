from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPageObjects:
    __username_field = (By.ID, "username")
    __password_field = (By.ID, "password")
    __submit_button = (By.ID, "submit")
    __login_success_text = (By.TAG_NAME, "h1")
    __logout_button = (By.LINK_TEXT, 'Log out')
    __login_error_text = (By.ID, "error")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_user_credentials(self, user_name, password):
        self.driver.find_element(*self.__username_field).send_keys(user_name)
        self.driver.find_element(*self.__password_field).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self.__submit_button).click()

    def get_login_success_text(self) -> str:
        return self.driver.find_element(*self.__login_success_text).text

    @property
    def get_current_url(self) -> str:
        return self.driver.current_url

    def is_logout_button_displayed(self):
        return self.driver.find_element(*self.__logout_button).is_displayed()

    def get_error_text(self) -> str:
        return self.driver.find_element(*self.__login_error_text).text
