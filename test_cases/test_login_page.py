from page_objects.login_page_objects import LoginPageObjects
from utilities.read_configuration import ReadConfiguration
from utilities.logger_config import LoggerConfiguration


class TestLoginPage:
    url = ReadConfiguration.get_url()
    user_name = ReadConfiguration.get_username()
    password = ReadConfiguration.get_password()
    logger = LoggerConfiguration.get_logger()

    def test_login_fun(self, get_driver):
        self.logger.info("******** Executing the test :: test_login_fun **********")
        driver = get_driver
        login_page = LoginPageObjects(driver)
        login_page.enter_user_credentials(self.user_name, self.password)
        login_page.click_login_button()
