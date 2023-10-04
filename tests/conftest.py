import threading

import pytest
from selenium import webdriver

from utils import logger_config, read_configuration

logger = logger_config.get_logger()


@pytest.fixture()
def get_driver(request, get_browser_name, get_application_url, driver=None):
    logger.info("****** initialising the browser driver *****")
    # browser = read_configuration.get_browser()
    # app_url = read_configuration.get_app_url()
    __browser = get_browser_name
    __url = get_application_url
    thread_driver = threading.local()
    thread_driver.driver = driver
    try:
        if thread_driver.driver is None:
            if __browser.__eq__("chrome"):
                logger.info("initializing the chrome browser")
                chrome_options = webdriver.ChromeOptions()
                driver = webdriver.Chrome(options=chrome_options)
                # driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", options=chrome_options)
            elif __browser.__eq__("firefox"):
                logger.info("initializing the {} browser".format(request.param))
                driver = webdriver.Firefox()
            elif __browser.__eq__("edge"):
                logger.info("initializing the {} browser".format(request.param))
                driver = webdriver.Edge()
            else:
                logger.info(f'browser {request.param} is not supported for this application')
            thread_driver.driver = driver
        thread_driver.driver.maximize_window()
        thread_driver.driver.set_page_load_timeout(15)
        thread_driver.driver.delete_all_cookies()
        thread_driver.driver.get(__url)
        yield thread_driver.driver
        logger.info("****** closing the browser driver ********")
        thread_driver.driver.quit()
    except Exception as e:
        logger.error("failed to initialize the webdriver :: get_driver", e)
        raise e


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
