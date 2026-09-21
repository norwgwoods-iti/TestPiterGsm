import time
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from src.utilities.logger import Logger


class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 3)
        self.actions = ActionChains(self.driver)

        self.base_url = 'https://pitergsm.ru/'


    # product_titles_xpath = '//a[@class="prodcard__name"]'
    # catalog_title_xpath = '//h1[@class="catalog__title"]'


    """ Method get current URL """
    def get_current_url(self):
        get_url = self.driver.current_url
        get_url = unquote(get_url)
        return f'current URL: {get_url}'


    """ Method get arguments NOT empty """
    @staticmethod
    def get_arguments_non_empty(arguments):
        non_empty_args = [
            value for key, value in arguments.items()
            if key != 'self' and value is not None
        ]
        return non_empty_args


    # Title page methods
    """ Method get Title Category """
    def get_title_category(self):
        catalog_title_xpath = '//h1[@class="catalog__title"]'
        catalog_title = self.wait.until(ec.visibility_of_element_located((By.XPATH, catalog_title_xpath))).text
        return catalog_title


    """ Method Get Titles Product """
    def get_product_titles(self, product_titles_list_xpath):
        time.sleep(1)
        product_titles = self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, product_titles_list_xpath)))
        titles = []
        for title in product_titles:
            titles.append(title.text)
        return titles


    @staticmethod
    def assertion_products_title(key_word: str | list, product_titles_list: str | list):
        titles = product_titles_list
        assert len(titles) > 0
        for key in key_word:
            assert any(key.lower() in title.lower() for title in titles)
        print('Search product success')



    """ Method assert price """
    def assert_price(self, expected_price, current_price):
        assert expected_price.text.replace(' ','').rstrip('₽') == current_price.text.replace(' ','').rstrip('₽')
        print('Success assert price')

    """ Method assert word """
    def assert_word(self, expected_word, current_word):
        assert expected_word.lower() == current_word.text.lower()
        print('Success assert word')

    """ Method assert title """
    def assert_title(self, expected_title):
        assert expected_title.lower() == self.get_title_category().lower()
        print('Success assert title')

    """ Method assert URL """
    def assert_url(self, expected_url):
        assert expected_url == unquote(self.driver.current_url), 'Error assert URL'
        print('Success assert URL')

    """ Method Screenshot """
    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d %H-%M-%S")
        screenshot_name = f'screenshot ({now_date}).png'
        current_dir = str(Path(__file__).resolve().parent.parent.parent / 'screenshots')
        time.sleep(1)
        self.driver.save_screenshot(f'{current_dir}/{screenshot_name}')
        print(f'Screenshot Saved: {screenshot_name}')

    """ Method is visible element """
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






