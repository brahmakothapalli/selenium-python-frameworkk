""" sample python tests"""
import time
import pytest
from page_objects.login_page_objects import LoginPageObjects


class TestParameterizedCases:
    """ login page tests"""

    @pytest.mark.login
    @pytest.mark.parametrize("scenario, username, password, expected_message", [("valid", "student", "Password123", "Logged In Successfully"),
                                                                                ("invalid", "student", "wrongpass", "Your password is invalid!")])
    def test_login_parameterization(self, get_driver, scenario,  username, password, expected_message):
        """validating login functionality"""
        login_page = LoginPageObjects(get_driver)
        login_page.enter_user_credentials(username, password)
        dashboard_page = login_page.click_login_button()
        if scenario == "valid":
            assert login_page.get_login_success_text() == expected_message, "login success message is not displayed"
            assert "logged-in-successfully" in login_page.get_current_url
            # assert dashboard_page.is_logout_button_displayed(), "logout button not displayed"
        else:
            time.sleep(3)
            assert login_page.get_error_text() == expected_message, "error message not displayed"
        print("***** Test successfully executed :: test_login_positive *****")
