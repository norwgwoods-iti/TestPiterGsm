from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from base.base_class import Base
class MacPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Check"""
    expected_title_imac_page = 'iMac'
    expected_imac_page_url = 'https://pitergsm.ru/catalog/mac/imac/'

    current_title_imac_page_xpath = '//h1[@class="catalog__title"]'


    # Locators

    imac_button_xpath = '(//a[contains(text(), "iMac")])[2]'


    # Getters

    def get_imac_button(self):
        return self.wait.until((ec.element_to_be_clickable((By. XPATH, self.imac_button_xpath))))

    def get_current_title_imac_page(self):
        return self.wait.until((ec.visibility_of_element_located((By. XPATH, self.current_title_imac_page_xpath))))


    # Actions

    def click_imac_button(self):
        self.get_imac_button().click()
        print('Click imac button')


    # Methods

    def select_category_imac(self):
        self.get_current_url()
        self.click_imac_button()
        self.assert_word(expected_word=self.expected_title_imac_page, current_word=self.get_current_title_imac_page())
        self.assert_url(expected_url=self.expected_imac_page_url)