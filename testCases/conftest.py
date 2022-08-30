from selenium import webdriver
import pytest


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser..................")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser..................")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config.metadata['Project Name'] = 'nop Commerce'
    config.metadata['Module name'] = 'Customers'
    config.metadata['Tester'] = 'Henry Aneke'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
