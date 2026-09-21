import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger


class CatalogPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.catalog_title_xpath = '//h1[@class="catalog__title"]'
        self.product_titles_xpath = '//a[@class="prodcard__name"]'


    # LOCATORS ________________________________________________________________________________

    @staticmethod
    def button_catalog_xpath(catalog):
        return f'//a[@class=" tags__tag"][(text()="{catalog}")]'

    """Add to cart"""
    add_to_cart_button_xpath = '(//button[@class="prodcard__btn btn btn_cta buy_link is_init"])[1]'
    cart_button_xpath = '//a[@class="btn btn_cta"]'

    # Getters
    def get_button_catalog(self, catalog):
        return self.wait.until((ec.element_to_be_clickable((By.XPATH, self.button_catalog_xpath(catalog)))))


    """Add to cart"""
    def get_add_to_cart_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_button_xpath)))

    def get_cart_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.cart_button_xpath)))


    # ACTIONS ________________________________________________________________________________


    def click_button_catalog(self, catalog):
        self.driver.execute_script('arguments[0].click();', self.get_button_catalog(catalog))
        print(f'Select catalog: "{catalog}"')


    """Add to cart"""
    def click_add_to_cart_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_add_to_cart_button())
        print('Click add cart button')

    def click_cart_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_cart_button())
        print('Click cart')


    # METHODS ________________________________________________________________________________


    def select_product_in_menu_catalog(self, catalog: str):
        with allure.step(f'Select menu catalog: "{catalog}"'):
            Logger.add_start_method(method='select_menu_catalog')
            self.click_button_catalog(catalog)
            self.assert_title(expected_title=catalog)
            self.assertion_products_title(
                key_word=catalog,
                product_titles_list=self.get_product_titles(self.product_titles_xpath))
            Logger.add_end_method(current_url=self.get_current_url(), method='select_menu_catalog')



    def add_product_to_cart(self):
        self.click_add_to_cart_button()
        self.click_cart_button()

        # assert