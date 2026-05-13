from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from datetime import datetime

from utilities.logger import Logger


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        self.actions = ActionChains(self.driver)

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        return f'current URL: {get_url}'

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
        self.driver.save_screenshot(f'./screen/{screenshot_name}')
        print(f'Screenshot Saved: {screenshot_name}')

    """Method is visible element"""
    def is_element_visible(self, locator, name_element):
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            Logger.write_log_to_file(f"INFO: {name_element} not available, switching to alternative.\n")
            return False

    """Method for visible/invisible filter button"""
    show_filter_button_xpath = '//label[@class="catalog__filter-trigger"]'

    def get_filter_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.show_filter_button_xpath)))

    def is_show_filter_button_visible(self):
        try:
            self.wait.until(ec.element_to_be_clickable((By.XPATH, self.show_filter_button_xpath)))
            return True
        except TimeoutException:
            Logger.write_log_to_file(f'INFO: filter button not visible\n')
            return False

    def click_filter_button_if_visible(self):
        if self.is_show_filter_button_visible():
            self.driver.execute_script('arguments[0].click();', self.get_filter_button())
            print('Click filter button')