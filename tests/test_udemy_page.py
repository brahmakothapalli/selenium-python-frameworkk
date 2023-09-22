''' sample python tests'''
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestLoginPage:
    ''' login page tests'''

    @pytest.mark.smoke
    def test_login_functionality(self):
        '''validating login functionality'''
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()

        user_name_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "submit")

        user_name_field.send_keys("student")    
        password_field.send_keys("Password123")
        submit_button.click()
        message = driver.find_element(By.TAG_NAME, "h1")
        success_message = message.text
        assert success_message == "Logged In Successfully"
        actual_url = driver.current_url
        assert "logged-in-successfully" in actual_url
        log_out_button = driver.find_element(By.LINK_TEXT, 'Log out')
        assert log_out_button.is_displayed(), "logout button not displayed"
        driver.quit()
        print("***** Test successfully executed *****")
