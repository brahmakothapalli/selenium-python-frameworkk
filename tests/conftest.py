import threading
from utils import read_configuration
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def get_driver(driver=None):
    print("****** initialising the browser driver *****")
    browser = read_configuration.get_browser()
    app_url = read_configuration.get_app_url()
    thread_driver = threading.local()
    thread_driver.driver = driver
    if thread_driver.driver is None:
        if browser.__eq__("chrome"):
            chrome_options = Options()
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=chrome_options)
        elif browser.__eq__("firefox"):
            driver = webdriver.Firefox()
        elif browser.__eq__("edge"):
            driver = webdriver.Edge()
        else:
            print(f'browser {browser} is not supported for this application')
        thread_driver.driver = driver
    thread_driver.driver.maximize_window()
    thread_driver.driver.set_page_load_timeout(15)
    thread_driver.driver.delete_all_cookies()
    thread_driver.driver.get(app_url)
    yield thread_driver.driver
    print("****** closing the browser driver ********")
    thread_driver.driver.quit()
