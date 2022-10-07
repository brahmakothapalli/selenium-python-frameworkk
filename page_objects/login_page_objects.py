from selenium.webdriver.common.by import By


class LoginPageObjects:
    user_name_id = (By.ID, "user-name")
    password_id = (By.ID, "password")
    login_button_id = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def enter_user_credentials(self, user_name, password):
        self.driver.find_element(*self.user_name_id).send_keys(user_name)
        self.driver.find_element(*self.password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button_id).click()
