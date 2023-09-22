import pytest
from selenium import webdriver
from utils.read_configuration import ReadConfiguration



@pytest.fixture()
def get_driver(get_browser):
    ''' returns browser driver'''
    driver = None
    if get_browser == "chrome" or get_browser is None:
        driver = webdriver.Chrome()
    elif get_browser == "firefox":
        driver = webdriver.Firefox()
    elif get_browser == "edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(ReadConfiguration.get_url())
    driver.implicitly_wait(15)
    return driver



def pytest_addoption(parser):
    """
    this method reads the options from commandline or hooks
    :param parser:
    :return:
    """
    parser.addoption("--browser")


@pytest.fixture()
def get_browser(request):
    '''returns browser type'''
    return request.config.getoption("--browser")


# to add info to pytest html report
def pytest_configure(config):
    ''' adding pytest report details'''
    config._metadata['Project Name'] = 'selenium-python-framework'
    config._metadata['Organization'] = 'QABABU Works'
    config._metadata['Author'] = "Brahma Rao Kothapalli"


# to delete/modify info in pytest html report
@pytest.mark.optionlhook
def pytest_metadata(metadata):
    '''pytest details'''
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Packages', None)


def capture_screenshot(driver):
    '''take the screenshot'''
    driver.get_screenshot_as_file("screenshots/page.png")
