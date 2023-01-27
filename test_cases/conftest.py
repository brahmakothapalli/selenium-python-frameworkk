import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utils.read_configuration import ReadConfiguration


@pytest.fixture()
def get_driver(get_browser):
    driver = None
    if get_browser == "chrome" or get_browser is None:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif get_browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif get_browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
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
    return request.config.getoption("--browser")


# to add info to pytest html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'selenium-python-framework'
    config._metadata['Organization'] = 'QABABU Works'
    config._metadata['Author'] = "Brahma Rao Kothapalli"


# to delete/modify info in pytest html report
@pytest.mark.optionlhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
    metadata.pop('Packages', None)


def capture_screenshot(driver):
    driver.get_screenshot_as_file("screenshots/page.png")
