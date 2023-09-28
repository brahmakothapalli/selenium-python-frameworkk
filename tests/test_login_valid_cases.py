""" sample python tests"""
import time
from ddt import ddt, data, unpack
import pytest

from page_objects.login_page_objects import LoginPageObjects


class TestValidLoginPageCases:
    """ login page tests"""

    @pytest.mark.login
    def test_login_positive(self, get_driver):
        """validating login functionality"""
        login_page = LoginPageObjects(get_driver)
        login_page.enter_user_credentials("student", "Password123")
        dashboard_page = login_page.click_submit_button()
        assert login_page.get_login_success_text() == "Logged In Successfully"
        assert "logged-in-successfully" in login_page.get_current_url
        assert dashboard_page.is_logout_button_displayed(), "logout button not displayed"
        print("***** Test successfully executed :: test_login_positive *****")

    @pytest.mark.login
    def test_login_negative(self, get_driver):
        """validating login functionality"""
        login_page = LoginPageObjects(get_driver)
        login_page.enter_user_credentials("student", "wrong password")
        login_page.click_submit_button()
        time.sleep(3)
        assert login_page.get_error_text() == "Your password is invalid!", "login error text not matched"
        print("***** Test successfully executed :: test_login_negative *****")
