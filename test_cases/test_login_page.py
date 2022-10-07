from page_objects.login_page_objects import LoginPageObjects


class TestLoginPage:
    url = "https://www.saucedemo.com/"
    user_name = "standard_user"
    password = "secret_sauce"

    def test_login_fun(self, get_driver):
        driver = get_driver
        login_page = LoginPageObjects(driver)
        login_page.enter_user_credentials(self.user_name, self.password)
        login_page.click_login_button()
