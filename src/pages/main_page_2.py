from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure
import time

from src.base.base_class import Base
from src.utilities.logger import Logger
from tests.test_data import catalog_data


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.base_url = 'https://pitergsm.ru/'

    # Locators

    @staticmethod
    def menu_catalog_button_xpath(catalog: str):
        return f'//a[@class="hcat__link js_hcat-sub-trigger"][contains(text(), "{catalog}")]'


    # Getters

    def get_menu_catalog_button(self, catalog: str):
        print(f'Click Menu catalog Button - "{catalog}"')
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.menu_catalog_button_xpath(catalog))))


    # Actions

    def click_menu_catalog_button(self, catalog: str):
        self.driver.execute_script('arguments[0].click();', self.get_menu_catalog_button(catalog))
        print(f'Select catalog - "{catalog}"')

    def open_url(self):
        self.driver.get(self.base_url)

    # Methods

    def select_menu_catalog(self, catalog: str):
        self.click_menu_catalog_button(catalog)
        self.assert_title(expected_title=catalog)
