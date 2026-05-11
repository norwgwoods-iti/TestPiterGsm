from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from base.base_class import Base
class AudioPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    """Check"""
    expected_title_headphones_page = 'Наушники'
    expected_headphones_page_url = 'https://pitergsm.ru/catalog/audio/naushniki/'
    current_title_headphones_page_xpath = '//h1[@class="catalog__title"]'


    # Locators

    headphones_button_xpath = '(//a[contains(text(), "Наушники")])[2]'


    # Getters

    def get_headphones_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.headphones_button_xpath)))

    def get_current_title_headphones_page(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.current_title_headphones_page_xpath)))


    # Actions

    def click_headphones_button(self):
        self.get_headphones_button().click()


    # Methods

    def select_category_headphones(self):
        self.get_current_url()
        self.click_headphones_button()
        self.assert_word(expected_word=self.expected_title_headphones_page, current_word=self.get_current_title_headphones_page())
        self.assert_url(self.expected_headphones_page_url)