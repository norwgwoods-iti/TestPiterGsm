from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators

    # name_product_xpath = '//a[@class="cart-prodcard__name"]'
    # price_product_cart_xpath = '//div[@class="cart-prodcard__price-current"]'
    order_button_xpath = '//a[@href="/personal/order/make/"]'


    # Getters

    def get_order_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.order_button_xpath)))


    # Actions

    def click_order_button(self):
        self.driver.execute_script("arguments[0].click();", self.get_order_button())


    # Methods

