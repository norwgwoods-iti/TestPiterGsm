import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from src.base.base_class import Base
from src.utilities.logger import Logger


class AudioPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    """Check"""
    expected_title_headphones_page = 'Наушники'
    expected_headphones_page_url = 'https://pitergsm.ru/catalog/audio/naushniki/'

    current_title_headphones_page_xpath = '//h1[@class="catalog__title"]'


    # Locators

    @staticmethod
    def headphones_button_xpath(category: str):
        return f'(//a[contains(text(), "{category}")])[2]'


    # headphones_button_xpath = '(//a[contains(text(), "Наушники")])[2]'


    # Getters

    def get_audio_category_button(self, category):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.headphones_button_xpath(category))))

    def get_current_title_headphones_page(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.current_title_headphones_page_xpath)))


    # Actions

    def click_headphones_button(self, category):
        self.driver.execute_script('arguments[0].click();', self.get_audio_category_button(category))
        print('Click headphones button')


    # Methods
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def select_category_headphones(self, category):
        with allure.step('Select category headphones page'):
            Logger.add_start_method(method='select_category_headphones')

            print(self.get_current_url())

            self.click_headphones_button(category)

            self.assert_word(expected_word=category, current_word=self.get_current_title_headphones_page())
            self.assert_url(self.expected_headphones_page_url)
            Logger.add_end_method(current_url=self.get_current_url(), method='select_category_headphones')

