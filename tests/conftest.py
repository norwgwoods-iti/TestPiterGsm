import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def set_up():
    print("Start Test")

    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument('guest')
    options.add_argument('--headless=new')
    # options.add_argument('start-maximized')

    driver = webdriver.Chrome(options=options)

    base_url = 'https://pitergsm.ru/'
    driver.get(base_url)
    # driver.maximize_window()

    yield driver

    driver.quit()
    print("Finish Test")
