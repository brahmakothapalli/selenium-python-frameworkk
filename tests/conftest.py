import threading

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import logger_config, read_configuration

logger = logger_config.get_logger()


@pytest.fixture()
def get_driver(request, get_browser_name, get_application_url, driver=None):
    logger.info("****** initialising the browser driver *****")
    # browser = read_configuration.get_browser()
    # app_url = read_configuration.get_app_url()
    _browser = get_browser_name
    _url = get_application_url
    thread_driver = threading.local()
    thread_driver.driver = driver
    if thread_driver.driver is None:
        if _browser.__eq__("chrome"):
            logger.info("initializing the chrome browser")
            chrome_options = Options()
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            driver = webdriver.Chrome(options=chrome_options)
        elif _browser.__eq__("firefox"):
            logger.info("initializing the {} browser".format(request.param))
            driver = webdriver.Firefox()
        elif _browser.__eq__("edge"):
            logger.info("initializing the {} browser".format(request.param))
            driver = webdriver.Edge()
        else:
            logger.info(f'browser {request.param} is not supported for this application')
        thread_driver.driver = driver
    thread_driver.driver.maximize_window()
    thread_driver.driver.set_page_load_timeout(15)
    thread_driver.driver.delete_all_cookies()
    thread_driver.driver.get(_url)
    yield thread_driver.driver
    logger.info("****** closing the browser driver ********")
    thread_driver.driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default=read_configuration.get_browser())
    parser.addoption("--url", action="store", default=read_configuration.get_app_url())


@pytest.fixture(autouse=True)
def get_browser_name(request):
    _browser = request.config.getoption("--browser")
    return _browser


@pytest.fixture(autouse=True)
def get_application_url(request):
    _url = request.config.getoption("--url")
    return _url
