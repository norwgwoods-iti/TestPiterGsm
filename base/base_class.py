from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(self.driver)

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'current URL: {get_url}')

    """Method assert price"""
    def assert_price(self, expected_price, current_price):
        assert expected_price.text.replace(' ','').rstrip('₽') == current_price.text.replace(' ','').rstrip('₽')
        print('Success assert price')

    """Method assert word"""
    def assert_word(self, expected_word, current_word):
        assert expected_word.lower() == current_word.text.lower()
        print('Success assert word')

    """Method assert URL"""
    def assert_url(self, expected_url):
        assert expected_url == self.driver.current_url
        print('Success assert URL')

    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d %H-%M-%S")
        screenshot_name = f'screenshot ({now_date}).png'
        time.sleep(1)
        self.driver.save_screenshot('/Users/nd/IT/Python/Training/PiterGsm/screen/' + screenshot_name)
        print('Screenshot Saved: ' + screenshot_name)



