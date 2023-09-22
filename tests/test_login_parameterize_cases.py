''' sample python tests'''
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestParameterizedCases:
    ''' login page tests'''

    @pytest.mark.login
    @pytest.mark.parametrize("scenario, username, password, expected_message", [("valid", "student", "Password123", "Logged In Successfully"),
                                                             (("invalid", "student", "wrongpass", "Your password is invalid!"))])
    def test_login_parameterization(self, get_driver,scenario,  username, password, expected_message):
        '''validating login functionality'''
        user_name_field = get_driver.find_element(By.ID, "username")
        password_field = get_driver.find_element(By.ID, "password")
        submit_button = get_driver.find_element(By.ID, "submit")
        user_name_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()
        if scenario is "valid":
            message_element = get_driver.find_element(By.TAG_NAME, "h1")
            success_message = message_element.text
            assert success_message.strip() == expected_message, "login success message is not displayed"
            actual_url = get_driver.current_url
            assert "logged-in-successfully" in actual_url
            log_out_button = get_driver.find_element(By.LINK_TEXT, 'Log out')
            assert log_out_button.is_displayed(), "logout button not displayed"
        else:
            time.sleep(3)
            error_element = get_driver.find_element(By.ID, "error")
            error_message = error_element.text
            assert error_message.strip() == expected_message, "error message not displayed"    
        print("***** Test successfully executed :: test_login_positive *****")

