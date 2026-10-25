import time
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import logging

logger = logging.getLogger(__name__)

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


    # """ Method get arguments NOT empty """
    # @staticmethod
    # def get_arguments_non_empty(arguments):
    #     non_empty_args = [
    #         value for key, value in arguments.items()
    #         if key != 'self' and value is not None
    #     ]
    #     return non_empty_args


    # Title page methods
    """ Method get Title Category """
    def get_title_category(self):
        catalog_title_xpath = '//h1[@class="catalog__title"]'
        catalog_title = self.wait.until(ec.visibility_of_element_located((By.XPATH, catalog_title_xpath))).text
        return catalog_title


    """ Method Get Titles Product """
    def get_product_title(self, product_title_xpath: str):
        time.sleep(1)
        product_title = self.wait.until(ec.visibility_of_element_located((By.XPATH, product_title_xpath)))
        return product_title.text
    #
    # """ Method Get Titles Product """
    # def get_product_titles(self, product_title_xpath):
    #     time.sleep(1)
    #     product_titles = self.wait.until(ec.visibility_of_all_elements_located((By.XPATH, product_title_xpath)))
    #     titles = []
    #     if isinstance(product_titles, list):
    #         for title in product_titles:
    #             titles.append(title.text)
    #         return titles
    #     else:
    #         return product_titles.text


    @staticmethod
    def assertion_products_title(key_word:str | list, product_title: str):
        assert len(product_title) > 0, 'Заголовк товара отсутствует'

        if isinstance(key_word, str):
            key_word = [key_word]

        assert any(word.lower() in product_title.lower() for word in key_word)

        logger.info('Success assertion_products_title')
    #
    # @staticmethod
    # def assertion_products_title(key_word: float | str | list, product_title: str | list):
    #     titles = product_title
    #     assert len(titles) > 0
    #     if isinstance(key_word, list):
    #         for key in key_word:
    #             if key:
    #                 assert any(key.lower() in title.lower() for title in titles)
    #     elif isinstance(key_word, str):
    #         assert any(key_word.lower() in title.lower() for title in titles)
    #     elif isinstance(key_word, float):
    #         assert any(key_word in title.lower() for title in titles)
    #
    #     logger.info('Success assertion_products_title')


    """ Method assert price """
    def assert_price(self, expected_price, current_price):
        assert expected_price.text.replace(' ','').rstrip('₽') == current_price.text.replace(' ','').rstrip('₽')
        logger.info('Success assert price')

    """ Method assert word """
    def assert_word(self, expected_word, current_word):
        assert expected_word.lower() == current_word.text.lower()
        logger.info('Success assert word')

    """ Method assert title """
    def assert_title(self, expected_title):
        assert expected_title.lower() == self.get_title_category().lower()
        logger.info('Success assert title')


    """ Method assert URL """
    def assert_url(self, expected_url):
        assert expected_url == unquote(self.driver.current_url), 'Error assert URL'
        logger.info('Success assert URL')

    """ Method Screenshot """
    def get_screenshot(self):
        now_date = datetime.now().strftime("%Y.%m.%d %H-%M-%S")
        screenshot_name = f'screenshot ({now_date}).png'
        current_dir = str(Path(__file__).resolve().parent.parent.parent / 'screenshots')
        time.sleep(1)
        self.driver.save_screenshot(f'{current_dir}/{screenshot_name}')
        logger.info('Screenshot success')


    """ Method is visible element """
    def is_element_visible(self, locator, name_element):
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            logger.exception("%s not available, switching to alternative.\n", name_element)
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
            logger.exception('Filter button not visible\n')
            return False

    def click_filter_button_if_visible(self):
        if self.is_show_filter_button_visible():
            self.driver.execute_script('arguments[0].click();', self.get_filter_button())
            logger.info('Click Filter button')






