import allure
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from base.base_class import Base
from utilities.logger import Logger


class CategoryPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.category_title_xpath = '//h1[@class="catalog__title"]'
        self.product_titles_xpath = '//a[@class="prodcard__name"]'


    # Locators

    @staticmethod
    def button_category_xpath(category):
        return f'//a[@class=" tags__tag"][(text()="{category}")]'

    """Add to cart"""
    add_to_cart_button_xpath = '(//button[@class="prodcard__btn btn btn_cta buy_link is_init"])[1]'
    cart_button_xpath = '//a[@class="btn btn_cta"]'

    # Getters
    def get_button_category(self, category):
        return self.wait.until((ec.element_to_be_clickable((By.XPATH, self.button_category_xpath(category)))))


    """Add to cart"""
    def get_add_to_cart_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_button_xpath)))

    def get_cart_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.cart_button_xpath)))

    # Actions
    def click_button_category(self, category):
        self.driver.execute_script('arguments[0].click();', self.get_button_category(category))
        print(f'Select category: "{category}"')


    """Add to cart"""
    def click_add_to_cart_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_add_to_cart_button())
        print('Click add cart button')

    def click_cart_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_cart_button())
        print('Click cart')

    # Methods

    def select_menu_category(self, category: str):
        with allure.step(f'Select menu category: "{category}"'):
            Logger.add_start_method(method='select_menu_category')
            self.click_button_category(category)
            self.assert_title(expected_title=category)
            self.assertion_products_title(
                key_word=category,
                product_titles_list=self.get_product_titles(self.product_titles_xpath))
            Logger.add_end_method(current_url=self.get_current_url(), method='select_menu_category')



    def add_product_to_cart(self):
        self.click_add_to_cart_button()
        self.click_cart_button()

        # assert