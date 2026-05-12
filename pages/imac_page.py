from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


from base.base_class import Base
from utilities.logger import Logger


class IMacPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Check"""
    expected_cart_url = 'https://pitergsm.ru/personal/cart/'
    expected_title_cart_page = 'Корзина'
    current_title_cart_page_xpath = '//h1[@class="section__title"]'

    price_product_catalog_xpath = '//div[@class="cart-prodcard__price-current"]'
    price_product_cart_xpath = '//div[@class="cart-prodcard__price-current"]'


    # Locators

    """Filters"""
    filter_xpath = '//div[@id="page-side"]'

    filter_memory_xpath = '//label[@data-tooltip="256GB"]'
    filter_ram_xpath = '//span[contains(text(), "8 GB")]'

    filter_color_dropdown_xpath = '(//button[@class="filter__block-trigger js_toggle_trigger isinit"])[6]'

    filter_color_xpath = '//label[@data-tooltip="Зеленый"]'
    filter_confirm_xpath = '//button[@id="modef"]'

    """Add to cart"""
    add_to_cart_button_xpath = '(//button[@class="prodcard__btn btn btn_cta buy_link is_init"])[1]'
    cart_button_xpath = '//a[@class="btn btn_cta"]'


    # Getters

    """Filters"""
    def get_filter_memory(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filter_memory_xpath)))

    def get_filter_ram(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filter_ram_xpath)))

    def get_filter_color_dropdown(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filter_color_dropdown_xpath)))
    def get_filter_color(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filter_color_xpath)))

    def get_filter_confirm(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filter_confirm_xpath)))

    """Add to cart"""
    def get_add_to_cart_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.add_to_cart_button_xpath)))

    def get_cart_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.cart_button_xpath)))

    """Check"""
    def get_price_product(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.price_product_catalog_xpath)))

    def get_price_product_cart(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.price_product_cart_xpath)))

    def get_current_title_cart_page(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.current_title_cart_page_xpath)))


    # Actions

    """Filters"""
    def click_filter_memory(self):
        self.driver.execute_script('arguments[0].click();', self.get_filter_memory())
        print('Click filter memory')

    def click_filter_ram(self):
        self.driver.execute_script('arguments[0].click();', self.get_filter_ram())
        print('Click filter ram')

    def click_filter_color_dropdown(self):
        self.driver.execute_script('arguments[0].click();', self.get_filter_color_dropdown())
        print('Click filter color drop')

    def click_filter_color(self):
        self.driver.execute_script('arguments[0].click();', self.get_filter_color())
        print('Click filter color')

    def click_filter_confirm(self):
        self.driver.execute_script('arguments[0].click();', self.get_filter_confirm())
        print('Click filter confirm')

    """Add to cart"""
    def click_add_to_cart_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_add_to_cart_button())
        print('Click add cart button')

    def click_cart_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_cart_button())
        print('Click cart')


    # Methods

    def filter_and_add_imac_to_cart(self):
        """Filters"""
        Logger.add_start_method(method='filter_and_add_imac_to_cart')
        print(self.get_current_url())
        self.click_filter_button_if_visible()
        self.click_filter_memory()
        self.click_filter_ram()
        self.click_filter_color_dropdown()
        self.click_filter_color()
        self.click_filter_confirm()
        """Add to cart"""
        self.click_add_to_cart_button()
        self.get_screenshot()
        self.click_cart_button()
        """Check"""
        self.assert_word(expected_word=self.expected_title_cart_page, current_word=self.get_current_title_cart_page())
        self.assert_url(expected_url=self.expected_cart_url)
        self.assert_price(expected_price=self.get_price_product(),current_price=self.get_price_product_cart())
        Logger.add_end_method(current_url=self.get_current_url(), method='filter_and_add_imac_to_cart')

