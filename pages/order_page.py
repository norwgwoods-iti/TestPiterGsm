from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

from base.base_class import Base
from utilities.logger import Logger


class OrderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)


    # Locators

    input_full_name_xpath = '//input[@placeholder="Ф.И.О."]'
    input_email_xpath = '//input[@placeholder="E-Mail"]'
    input_phone_number_xpath = '//input[@placeholder="Телефон"]'

    """Delivery"""
    delivery_button_xpath = '//button[contains(text(), "Доставка")]'

    input_city_address_xpath = '//input[@placeholder="Город, улица, дом"]'
    input_entrance_xpath = '//input[@placeholder="Подъезд"]'
    input_floor_xpath = '//input[@placeholder="Этаж"]'
    input_apartment_xpath = '//input[@placeholder="Квартира"]'

    address_confirm_button_xpath = '//div[@id="closeBalloonBtn"]'

    choice_day_delivery_button_xpath = '//span[contains(text(), "завтра")]'
    choice_time_delivery_button_xpath = '(//span[contains(text(), "19:00 до 23:00")])[1]'

    """Pay"""
    payment_button_xpath = '//span[@class="pills__pill-text pay_system_button"]'

    """Checkout"""
    checkout_information_xpath = '//*[@id="bx-soa-order-form"]/div/div[2]/div[2]/div[1]/div[1]/div/p'
    final_price_xpath = '//span[@class="m-nowrap js-order-price"]'
    element_screenshot_xpath = '//h3[@class="checkout__list-title"]'

    confirm_order_button_xpath = '//button[contains(text(), "Оформить заказ")]'


    # Getters

    """Input Contact Info"""
    def get_input_full_name(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_full_name_xpath)))

    def get_input_email(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_email_xpath)))

    def get_input_phone_number(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_phone_number_xpath)))

    """Input Delivery Info"""
    def get_delivery_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.delivery_button_xpath)))

    def get_input_city_address(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_city_address_xpath)))

    def get_input_entrance(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_entrance_xpath)))

    def get_input_floor(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_floor_xpath)))

    def get_input_apartment(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_apartment_xpath)))

    def get_address_confirm_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.address_confirm_button_xpath)))


    def get_choice_day_delivery_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.choice_day_delivery_button_xpath)))

    def get_choice_time_delivery_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.choice_time_delivery_button_xpath)))

    """Pay"""
    def get_payment_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.payment_button_xpath)))

    """Checkout"""
    def get_checkout_information(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.checkout_information_xpath)))

    def get_final_price(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.final_price_xpath)))

    def get_confirm_order_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.confirm_order_button_xpath)))

    """Move to screenshot element"""
    def get_element_screenshot(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.element_screenshot_xpath)))


    # Actions

    """Input Contact Info"""
    def input_full_name(self, full_name):
        self.get_input_full_name().send_keys(full_name)
        print('Input full name')

    def input_email(self, mail):
        self.get_input_email().send_keys(mail)
        print('Input email')

    def input_phone_number(self, phone_number):
        self.get_input_phone_number().send_keys(phone_number)
        print('Input phone number')

    """Input Delivery Info"""
    def click_delivery_button(self):
        self.get_delivery_button().click()
        print('Click delivery button')

    def input_city_address(self, city_address):
        self.get_input_city_address().send_keys(city_address)
        self.get_input_city_address().send_keys(Keys.ARROW_DOWN)
        self.get_input_city_address().send_keys(Keys.RETURN)
        print('Input city address')

    def input_entrance(self, entrance):
        self.get_input_entrance().send_keys(entrance)
        print('Input entrance')

    def input_floor(self, floor):
        self.get_input_floor().send_keys(floor)
        print('Input floor')

    def input_apartment(self, apartment):
        self.get_input_apartment().send_keys(apartment)
        print('Input apartment')

    def click_address_confirm_button(self):
        self.get_address_confirm_button().click()
        print('Click address confirm button')


    def click_choice_day_delivery_button(self):
        self.get_choice_day_delivery_button().click()
        print('Click choice day delivery button')

    def click_choice_time_delivery_button(self):
        self.get_choice_time_delivery_button().click()
        print('Click choice time delivery button')

    """Pay"""
    def click_payment_button(self):
        self.get_payment_button().click()
        print('Click payment button')

    """Checkout"""
    def show_checkout_information(self):
        print(f'Способ получчения: {self.get_checkout_information().text}')

    def show_final_price(self):
        print(f' К оплате: {self.get_final_price().text}')

    def click_confirm_order_button(self):
        self.get_confirm_order_button().click()
        print('Click confirm order button')

    """Move to screenshot element"""
    def move_to_screenshot_element(self):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.get_element_screenshot())


    # Methods

    """Input Contact Info"""
    def input_information(self, full_name, email, phone_number):
        Logger.add_start_step(method='input_information')
        self.get_current_url()
        self.input_full_name(full_name)
        self.input_email(email)
        self.input_phone_number(phone_number)
        Logger.add_end_step(url=self.get_current_url(), method='input_information')

    """Input Delivery Info"""
    def input_delivery_information(self, city_address, entrance, floor, apartment):
        Logger.add_start_step(method='input_delivery_information')
        self.click_delivery_button()
        self.input_city_address(city_address)
        self.input_entrance(entrance)
        self.input_floor(floor)
        self.input_apartment(apartment)
        self.click_address_confirm_button()
        self.click_choice_day_delivery_button()
        self.click_choice_time_delivery_button()
        self.click_payment_button()
        Logger.add_end_step(url=self.get_current_url(), method='input_delivery_information')

    """Checkout"""
    def checkout_information(self):
        Logger.add_start_step(method='checkout_information')
        self.show_checkout_information()
        self.show_final_price()
        self.move_to_screenshot_element()
        self.get_screenshot()
        # self.click_confirm_order_button()
        Logger.add_end_step(url=self.get_current_url(), method='checkout_information')




