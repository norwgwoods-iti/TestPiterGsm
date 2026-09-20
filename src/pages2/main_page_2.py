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


    # LOCATORS ________________________________________________________________________________________

    @staticmethod
    def menu_catalog_button_xpath(catalog: str):
        return f'//a[@class="hcat__link js_hcat-sub-trigger"][contains(text(), "{catalog}")]'

    cookie_button = '//button[@id="cookie-consent-btn"]'


    """ Check (Asserts) """
    expected_main_logo_src = 'https://pitergsm.ru/local/templates/main/assets/img/pitergsm_color_c.svg'

    main_logo_xpath = '//img[@class="header__logo-img"]'

    # GETTERS ________________________________________________________________________________________

    def get_menu_catalog_button(self, catalog: str):
        print(f'Click Menu catalog Button - "{catalog}"')
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.menu_catalog_button_xpath(catalog))))

    """ Cookie """
    def get_cookie_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.cookie_button)))


    """ Check (Asserts) """
    def get_src_main_logo(self):
        title_src_image = self.wait.until(ec.visibility_of_element_located((By.XPATH, self.main_logo_xpath)))
        return title_src_image.get_attribute('src')


    # ACTIONS ________________________________________________________________________________________

    def click_menu_catalog_button(self, catalog: str):
        self.driver.execute_script('arguments[0].click();', self.get_menu_catalog_button(catalog))
        print(f'Select catalog: "{catalog}"')

    """ Cookie """
    def click_cookie_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_cookie_button())
        print('Click Cookie Button')


    """ Check (Asserts) """
    def assert_main_logo(self):
        assert self.get_src_main_logo() == self.expected_main_logo_src
        print('Success Assert main logo')

    # METHODS ________________________________________________________________________________________


    def open_url(self):
        with allure.step('Open main page'):
            Logger.add_start_method(method='open_main_page')

            self.driver.get(self.base_url)
            self.click_cookie_button()

            self.assert_url(expected_url=self.base_url)
            self.assert_main_logo()

            Logger.add_end_method(method='open_main_page', current_url=self.get_current_url())



    def select_menu_catalog(self, catalog: str):
        with allure.step(f'Select catalog: "{catalog}"'):
            Logger.add_start_method(method='select_catalog')

            self.click_menu_catalog_button(catalog)

            self.assert_title(expected_title=catalog)

            Logger.add_end_method(method='select_catalog', current_url=self.get_current_url())
