import logging
import time
from datetime import datetime
from pathlib import Path
from src.utilities.logging_config import setup_logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from src.utilities.test_markers import log_test_start, log_test_end

logger = logging.getLogger(__name__)

LOG_DIR = Path(__file__).resolve().parent.parent / 'logs'

def pytest_configure(config):
    log_file_path = setup_logging(LOG_DIR)

    print(f'Logging to {log_file_path}')


@pytest.fixture(autouse=True)
def log_test_markers(request):                              # ← снова без driver
    log_test_start(request.node.nodeid, request.node.name)
    yield
    url = next(
        (v for k, v in request.node.user_properties if k == 'current_url'),
        'n/a',
    )
    log_test_end(request.node.nodeid, url)

def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Choose browser: chrome or firefox',
    )


@pytest.fixture(scope='function')
def driver(request):
    name_browser = request.config.getoption('--browser')
    logger.info('Start Test in %s', name_browser.capitalize())

    if name_browser == 'chrome':
        options = ChromeOptions()
        options.add_argument('--guest')
        options.add_argument('--headless=new')
        driver = webdriver.Chrome(options=options)
    elif name_browser == 'firefox':
        options = FirefoxOptions()
        options.add_argument('-headless')
        driver = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser must be chrome or firefox')

    yield driver

    try:
        request.node.user_properties.append(('current_url', driver.current_url))
    except Exception:
        pass
    time.sleep(8)
    driver.quit()
    logger.info('Quit Browser')
    logger.info('Finish Test in %s', name_browser.capitalize())