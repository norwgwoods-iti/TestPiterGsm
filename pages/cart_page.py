from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base
from utilities.logger import Logger


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Check"""
    expected_order_url = 'https://pitergsm.ru/personal/order/make/'
    expected_title_order_page = 'Оформление заказа'
    current_title_order_page_xpath = '//h1[@class="section__title"]'


    # Locators

    name_product_xpath = '//a[@class="cart-prodcard__name"]'
    price_product_cart_xpath = '//div[@class="cart-prodcard__price-current"]'
    order_button_xpath = '(//a[@class="btn btn_cta"])[1]'


    # Getters

    def get_name_product(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.name_product_xpath)))

    def get_price_product(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.price_product_cart_xpath)))

    def get_order_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.order_button_xpath)))

    """Check"""
    def get_current_title_order_page(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.current_title_order_page_xpath)))


    # Actions

    def click_order_button(self):
        self.get_order_button().click()
        print('Clicked checkout button')


    # Methods

    def select_order(self):
        Logger.add_start_step(method='select_order')
        print(f'{self.get_name_product().text}: {self.get_price_product().text}')
        self.click_order_button()
        self.assert_word(expected_word=self.expected_title_order_page, current_word=self.get_current_title_order_page())
        self.assert_url(expected_url=self.expected_order_url)
        Logger.add_end_step(url=self.get_current_url(), method='select_order')


