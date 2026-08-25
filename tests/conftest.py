import allure
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', help='Choose browser: chrome or firefox')

@pytest.fixture(scope="function")
def set_up(request):
    name_browser = request.config.getoption("--browser")
    if name_browser == "chrome":
        print('Start Test in Chrome')
        options = ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument('guest')
        # options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
    elif name_browser == "firefox":
        print('Start Test in Firefox')
        options = FirefoxOptions()
        options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser must be chrome or firefox')
    yield driver
    print("Quit Browser")
    driver.quit()
    print("Finish Test")

#  --tb=line - короткий отчет по тесту в консоли