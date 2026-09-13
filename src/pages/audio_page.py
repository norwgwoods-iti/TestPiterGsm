import allure
from transliterate import translit

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from src.base.base_class import Base
from src.utilities.logger import Logger


class AudioPage(Base):
    def __init__(self, driver):
        super().__init__(driver)


    """Check"""
    # expected_title_headphones_page = 'Наушники'

    audio_page_url = 'https://pitergsm.ru/catalog/audio'

    def expected_subcategory_url(self, subcategory):
        subcategory_result = translit(subcategory, 'ru', reversed=True)
        expected_subcategory_url = f'{self.audio_page_url}/{subcategory_result.lower()}/'
        return expected_subcategory_url


    # Locators

    @staticmethod
    def headphones_button_xpath(category: str):
        return f'(//a[contains(text(), "{category}")])[2]'


    # Getters

    def get_audio_subcategory_button(self, category):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.headphones_button_xpath(category))))

    def get_current_title_page(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.catalog_title_xpath)))


    # Actions

    def click_subcategory_button(self, category):
        self.driver.execute_script('arguments[0].click();', self.get_audio_subcategory_button(category))
        print('Click headphones button')


    # Methods
    def select_subcategory(self, category):
        with allure.step('Select category headphones page'):
            Logger.add_start_method(method='select_category_headphones')

            print(self.get_current_url())

            self.click_subcategory_button(category)

            self.assert_word(expected_word=category, current_word=self.get_current_title_page())

            print(self.expected_subcategory_url(category))

            self.assert_url(self.expected_subcategory_url(category))

            Logger.add_end_method(current_url=self.get_current_url(), method='select_category_headphones')

