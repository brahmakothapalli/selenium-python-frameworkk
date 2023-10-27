from page_objects.login_page_objects import LoginPageObjects
import pytest


class TestLoginPageScenarios:
    """ login page tests"""

    # class name must start with "Test"

    @pytest.mark.login
    def test_login_positive(self, get_driver):
        """validating login functionality"""
        login_page = LoginPageObjects(get_driver)
        login_page.enter_user_credentials("standard_user", "secret_sauce")
        products_page = login_page.click_submit_button()
        assert products_page.is_products_page_displayed(), "Products page is not displayed"
        assert products_page.get_products_page_text() == "Products", "Products page text not matched"
        print("***** Test successfully executed :: test_login_positive *****")

    @pytest.mark.login
    def test_login_negative(self, get_driver):
        """validating login functionality"""
        login_page = LoginPageObjects(get_driver)
        login_page.enter_user_credentials("student", "wrong password")
        login_page.click_submit_button()
        assert login_page.get_error_text() == "Epic sadface: Username and password do not match any user in this service", "login error text not matched"
        print("***** Test successfully executed :: test_login_negative *****")
