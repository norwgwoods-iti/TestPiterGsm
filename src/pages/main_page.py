from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure
import time

from src.base.base_class import Base
from src.utilities.logger import Logger


class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Check"""

    expected_title_image_src = 'https://pitergsm.ru/local/templates/main/assets/img/pitergsm_color_c.svg'

    product_titles_xpath = '//a[@class="digi-product__label"]'

    expected_title_mac_page = 'Mac'
    expected_mac_page_url = 'https://pitergsm.ru/catalog/mac/'
    current_title_mac_page_xpath = '//h1[@class="catalog__title"]'

    expected_title_audio_page = 'Аудио'
    expected_audio_page_url = 'https://pitergsm.ru/catalog/audio/'
    current_title_audio_page_xpath = '//h1[@class="catalog__title"]'

    # check url with search
    @staticmethod
    def expected_search_url(product_name: str | list):

        product_url = product_name.split(' ')

        list_url = []
        i = 1
        list_url.append(product_url[0])
        while i < len(product_url):
            list_url.append(f'%20{product_url[i]}')
            i += 1

        result = "".join(list_url)

        return f'https://pitergsm.ru/?digiSearch=true&term={result}&params=%7Csort%3DDEFAULT'



    # Locators

    cookie_button = '//button[@id="cookie-consent-btn"]'

    title_page_xpath = '//img[@class="header__logo-img"]'

    menu_category_mac_button_xpath = '(//a[@class="hcat__link js_hcat-sub-trigger"])[3]'

    menu_category_audio_button_xpath = '(//a[@class="hcat__link js_hcat-sub-trigger"])[5]'

    search_input_xpath = '//input[@placeholder="Поиск"]'
    search_button_xpath = '//button[@class="searchbox__btn"]'


    # Getters

    """Cookie"""
    def get_cookie_button(self):
        return self.wait.until(ec.element_to_be_clickable((By. XPATH, self.cookie_button)))

    """ Title """
    def get_src_title_main_page(self):
        title_src_image = self.wait.until(ec.visibility_of_element_located((By. XPATH, self.title_page_xpath)))
        return title_src_image.get_attribute('src')

    """Take Mac"""
    def get_category_mac_button(self):
        return self.wait.until((ec.element_to_be_clickable((By. XPATH, self.menu_category_mac_button_xpath))))

    def get_current_title_mac_page(self):
        return self.wait.until((ec.visibility_of_element_located((By. XPATH, self.current_title_mac_page_xpath))))

    """Take Headphone"""
    def get_category_audio_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.menu_category_audio_button_xpath)))

    def get_current_title_audio_page(self):
        return self.wait.until(ec.visibility_of_element_located((By. XPATH, self.current_title_audio_page_xpath)))


    """ Search Product """
    def get_search_input(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.search_input_xpath)))

    def get_search_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.search_button_xpath)))

    """ Title Search Products """
    def get_product_titles(self):
        time.sleep(1)
        product_titles = self.wait.until(ec.visibility_of_all_elements_located((By. XPATH, self.product_titles_xpath)))
        titles = []
        for title in product_titles:
            titles.append(title.text)
        return titles

    # Actions

    """Cookie"""
    def click_cookie_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_cookie_button())
        print('Click Cookie Button')

    """ Title """
    def check_assertion_main_title(self):
        assert self.get_src_title_main_page() == self.expected_title_image_src
        print('Check assertion main title')

    """Take Mac"""
    def click_category_mac_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_category_mac_button())
        print('Click Menu Category Button')

    """Take Headphone"""
    def click_category_audio_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_category_audio_button())
        print('Click Menu Audio Button')

    """ Search Product """
    # in find_product ->
    def send_search_input(self, product_name):
        self.get_search_input().clear()
        self.get_search_input().send_keys(product_name)
        print(f'Input: {product_name}')
    # in find_product ->
    def click_search_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_search_button())
        print('Click search button')

    def find_product(self, product_name):
        self.send_search_input(product_name)
        self.click_search_button()
        print(f'Find Product:{product_name}')

    def assertion_products_title(self, product_name: str | list):
        titles = self.get_product_titles()
        assert len(titles) > 0
        assert any(product_name.lower() in title.lower() for title in titles)
        print('Search product success')

    # Methods

    """Take Mac"""
    def select_category_mac(self):
        with allure.step('Select Category Mac'):
            Logger.add_start_method(method='select_category_mac')
            print(self.get_current_url())
            self.click_cookie_button()
            self.click_category_mac_button()
            self.assert_word(expected_word=self.expected_title_mac_page, current_word=self.get_current_title_mac_page())
            self.assert_url(expected_url=self.expected_mac_page_url)
            Logger.add_end_method(current_url=self.get_current_url(), method='select_category_mac')


    """Take Headphone"""
    def select_category_audio(self):
        with allure.step('Select Category Audio'):
            Logger.add_start_method(method='select_category_audio')
            print(self.get_current_url())
            self.click_cookie_button()
            self.click_category_audio_button()
            self.assert_word(expected_word=self.expected_title_audio_page, current_word=self.get_current_title_audio_page())
            self.assert_url(expected_url=self.expected_audio_page_url)
            Logger.add_end_method(current_url=self.get_current_url(), method='select_category_audio')

    """ Search Product """
    def search_product(self, product_name):
        with allure.step(f'Search product: {product_name}'):
            Logger.add_start_method(method='search_product')

            print(self.get_current_url())

            self.click_cookie_button()
            self.find_product(product_name)

            time.sleep(0.5)  # url меняется не так быстро

            print(self.get_current_url())
            print(self.expected_search_url(product_name))

            self.assert_url(MainPage.expected_search_url(product_name))

            self.assertion_products_title(product_name)

            Logger.add_end_method(current_url=self.get_current_url(), method='search_product')