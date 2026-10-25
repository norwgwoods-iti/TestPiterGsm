import time

import allure
from selenium.webdriver import Keys

from src.base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from tests.test_data.order_data import ORDER_CONTACT_INFO
import logging

logger = logging.getLogger(__name__)

class OrderPage(Base):


    # LOCATORS

    """Input Contact Info"""
    input_full_name_xpath = '//input[@placeholder="Ф.И.О."]'
    input_email_xpath = '//input[@placeholder="E-Mail"]'
    input_phone_number_xpath = '//input[@placeholder="Телефон"]'


    @staticmethod
    def method_preparation_xpath(preparation: str):
        return f'//button[contains(text(), "{preparation}")]'


    """Input Delivery Info (Address)"""
    # delivery_button_xpath = '//button[contains(text(), "Доставка")]'


    input_city_address_xpath = '//input[@placeholder="Город, улица, дом"]'
    input_entrance_xpath = '//input[@placeholder="Подъезд"]'
    input_floor_xpath = '//input[@placeholder="Этаж"]'
    input_apartment_xpath = '//input[@placeholder="Квартира"]'

    address_confirm_button_xpath = '//div[@id="closeBalloonBtn"]'

    xpath = '//span[contains(text(), "                         1-комнатная                     ")]'

    """ Set datetime delivery """
    def day_to_delivery_button_xpath(self):
        today_button_xpath = '//span[contains(text(), "сегодня")]'
        tomorrow_button_xpath = '//span[contains(text(), "завтра")]'
        if self.is_element_visible(today_button_xpath, 'Today delivery button'):
            return today_button_xpath

        elif self.is_element_visible(tomorrow_button_xpath, 'Tomorrow delivery button'):
            return tomorrow_button_xpath

        raise AssertionError(
            'Today and Tomorrow delivery buttons not found. Please check your input and try again.'
        )

    choice_time_delivery_button_xpath = '//span[contains(text(), " до ")]'

    """ Pay """
    payment_button_xpath = '//span[@class="pills__pill-text pay_system_button"]'


    """ Checkout """
    checkout_information_xpath = '//*[@id="bx-soa-order-form"]/div/div[2]/div[2]/div[1]/div[1]/div/p'
    final_price_xpath = '//span[@class="m-nowrap js-order-price"]'
    # element_screenshot_xpath = '//h3[@class="checkout__list-title"]'


    """ Confirm Order """
    confirm_order_button_xpath = '//button[contains(text(), "Оформить заказ")][@type="submit"]'

    # GETTERS _____________________________________________________________________

    """ Input Contact Info """
    def get_input_full_name(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_full_name_xpath)))
    def get_input_email(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_email_xpath)))
    def get_input_phone_number(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.input_phone_number_xpath)))


    """ Choice Preparation Method """
    def get_preparation_method_button(self, preparation: str):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.method_preparation_xpath(preparation))))


    """ Input Delivery Info (Address) """
    def get_input_city_address(self):
        return self.wait.until((ec.element_to_be_clickable((By.XPATH, self.input_city_address_xpath))))
    def get_input_entrance(self):
        return self.wait.until((ec.element_to_be_clickable((By.XPATH, self.input_entrance_xpath))))
    def get_input_floor(self):
        return self.wait.until((ec.element_to_be_clickable((By.XPATH, self.input_floor_xpath))))
    def get_input_apartment(self):
        return self.wait.until((ec.element_to_be_clickable((By.XPATH, self.input_apartment_xpath))))

    def get_address_confirm_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.address_confirm_button_xpath)))

    """ Set datetime delivery """
    def get_day_to_delivery_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.day_to_delivery_button_xpath())))
    def get_choice_time_delivery_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.choice_time_delivery_button_xpath)))


    """ Pay """
    def get_payment_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.payment_button_xpath)))


    """ Checkout """

    def get_checkout_information(self):
        return self.wait.until(ec.visibility_of_element_located((By.XPATH, self.checkout_information_xpath)))

    def get_final_price(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.final_price_xpath)))


    """ Confirm Order """
    def get_confirm_order_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.confirm_order_button_xpath)))




    # ACTIONS _____________________________________________________________________

    """Input Contact Info"""
    def input_full_name(self):
        self.get_input_full_name().send_keys(ORDER_CONTACT_INFO['full_name'])
        logger.info('Input full name')
        # print('Input full name')
    def input_email(self):
        self.get_input_email().send_keys(ORDER_CONTACT_INFO['email'])
        logger.info('Input email')
        # print('Input email')
    def input_phone_number(self):
        self.get_input_phone_number().send_keys(ORDER_CONTACT_INFO['phone_number'])
        logger.info('Input phone number')
        # print('Input phone number')


    """ Choice Preparation Method """
    def click_preparation_method_button(self, preparation):
        self.driver.execute_script('arguments[0].click();', self.get_preparation_method_button(preparation))
        time.sleep(1)
        logger.info('Click preparation method')
        # print('Click preparation method')


    """ Input Delivery Info (Address) """
    def input_city_address(self):
        self.get_input_city_address().send_keys(ORDER_CONTACT_INFO['city_address'])
        self.get_input_city_address().send_keys(Keys.ARROW_DOWN)
        self.get_input_city_address().send_keys(Keys.RETURN)
        logger.info('Input city_address')
        # print('Input city address')
    def input_entrance(self):
        self.get_input_entrance().send_keys(ORDER_CONTACT_INFO['entrance'])
        logger.info('Input entrance')
        # print('Input entrance')
    def input_floor(self):
        self.get_input_floor().send_keys(ORDER_CONTACT_INFO['floor'])
        # print('Input floor')
        logger.info('Input floor')
    def input_apartment(self):
        self.get_input_apartment().send_keys(ORDER_CONTACT_INFO['apartment'])
        # print('Input apartment')
        logger.info('Input apartment')


    def click_address_confirm_button(self):
        time.sleep(1)
        self.driver.execute_script('arguments[0].click();', self.get_address_confirm_button())
        logger.info('Click Address confirm button')
        # print('Click address confirm button')


    """ Set datetime delivery """
    def click_day_to_delivery_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_day_to_delivery_button())
        logger.info('Click Day to delivery button')
        # print('Click day to delivery button')
    def click_choice_time_delivery_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_choice_time_delivery_button())
        logger.info('Click Choice Time delivery button')
        # print('Click choice time delivery button')


    """ Pay """
    def click_payment_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_payment_button())
        logger.info('Click Payment button')
        # print('Click Pay button')


    """ Checkout """
    def show_checkout_information(self):
        logger.info(f'Способ получения: %s', self.get_checkout_information().text)

    def show_final_price(self):
        # print(f' К оплате: {self.get_final_price().text}')
        logger.info(f'К оплате: %s', self.get_final_price().text)


    """ Confirm order """
    def click_confirm_order_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_confirm_order_button())
        logger.info('Click confirm order')
        # print('Click Confirm order')


    # METHODS _____________________________________________________________________

    """Input Contact Info"""
    def input_contact_info(self):
        with allure.step('Input Contact Info'):
            logger.info('<-- Start Input Contact Info')
            self.input_full_name()
            self.input_email()
            self.input_phone_number()
            logger.info('<-- End Input Contact Info. %s', self.get_current_url())


    """ Self-pickup """
    # Самовывоз


    """ Delivery """
    """Input Delivery Info (Address)"""
    def input_delivery_info(self):
        with allure.step('Input Delivery Info'):
            logger.info('<-- Start Input Delivery Info')
            self.input_city_address()
            self.input_entrance()
            self.input_floor()
            self.input_apartment()
            self.click_address_confirm_button()
            logger.info('<-- End Input Delivery Info. %s', self.get_current_url())

    """ Set datetime delivery """
    def set_datetime_delivery(self):
        with allure.step('Set datetime delivery'):
            logger.info('<-- Start Set datetime delivery')
            self.click_day_to_delivery_button()
            self.click_choice_time_delivery_button()
            logger.info('<-- End Set datetime delivery. %s', self.get_current_url())

    def delivery_method(self):
        with allure.step('Delivery method'):
            logger.info('<-- Start Delivery method')
            self.input_delivery_info()
            self.set_datetime_delivery()
            logger.info('<-- End Delivery method. %s', self.get_current_url())


    """ Express Delivery """
    # Экспресс-доставка


    """ Checkout """
    def checkout_information(self):
        with allure.step('Checkout Information'):
            logger.info('<-- Start Checkout Information')
            self.show_checkout_information()
            self.show_final_price()
            logger.info('<-- End Checkout Information. %s', self.get_current_url())


    def choice_preparation_method(self, preparation: str):
        if preparation == 'Самовывоз':
            pass
        if preparation == 'Доставка':
            self.delivery_method()
        if preparation == 'Экспресс доставка':
            self.delivery_method()


    """ Main """
    def buy_product(self, preparation: str):
        with allure.step('Buy Product'):
            logger.info('<-- Start Buy Product. Category: %s', preparation)
            self.input_contact_info()
            self.click_preparation_method_button(preparation)
            self.choice_preparation_method(preparation)
            self.click_payment_button()
            self.checkout_information()
            # self.click_confirm_order_button()
            logger.info('<-- End Buy Product.  Category: %s. %s', preparation, self.get_current_url())
