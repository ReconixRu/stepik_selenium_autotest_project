import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb",
                     help="Choose language (default: en-gb)")


@pytest.fixture(scope="function")
def browser(request):
    # https://stepik.org/lesson/213670/step/2?discussion=1319467&unit=186864 - тестирование в фоне
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    time.sleep(10)
    browser.quit()

@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("language")
