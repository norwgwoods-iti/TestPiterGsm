import time

from selenium.webdriver import Keys

from src.base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

from tests.test_data.order_data import ORDER_CONTACT_INFO

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

    """ Set datetime delivery """
    def day_to_delivery_button_xpath(self):
        today_button_xpath = '//span[contains(text(), "сегодня")]'
        tomorrow_button_xpath = '//span[contains(text(), "завтра")]'
        if self.is_element_visible(today_button_xpath, 'Today delivery button'):
            return today_button_xpath

        if self.is_element_visible(tomorrow_button_xpath, 'Tomorrow delivery button'):
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
        print('Input full name')
    def input_email(self):
        self.get_input_email().send_keys(ORDER_CONTACT_INFO['email'])
        print('Input email')
    def input_phone_number(self):
        self.get_input_phone_number().send_keys(ORDER_CONTACT_INFO['phone_number'])
        print('Input phone number')


    """ Choice Preparation Method """
    def click_preparation_method_button(self, preparation):
        time.sleep(1)
        self.driver.execute_script('arguments[0].click();', self.get_preparation_method_button(preparation))


    """ Input Delivery Info (Address) """
    def input_city_address(self):
        self.get_input_city_address().send_keys(ORDER_CONTACT_INFO['city_address'])
        self.get_input_city_address().send_keys(Keys.ARROW_DOWN)
        self.get_input_city_address().send_keys(Keys.RETURN)
    def input_entrance(self):
        self.get_input_entrance().send_keys(ORDER_CONTACT_INFO['entrance'])
    def input_floor(self):
        self.get_input_floor().send_keys(ORDER_CONTACT_INFO['floor'])
    def input_apartment(self):
        self.get_input_apartment().send_keys(ORDER_CONTACT_INFO['apartment'])

    def click_address_confirm_button(self):
        time.sleep(1)
        self.driver.execute_script('arguments[0].click();', self.get_address_confirm_button())
        print('Click address confirm button')

    """ Set datetime delivery """
    def click_day_to_delivery_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_day_to_delivery_button())
    def click_choice_time_delivery_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_choice_time_delivery_button())


    """ Pay """
    def click_payment_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_payment_button())


    """ Checkout """
    def show_checkout_information(self):
        print(f'Способ получения: {self.get_checkout_information().text}')

    def show_final_price(self):
        print(f' К оплате: {self.get_final_price().text}')


    """ Confirm order """
    def click_confirm_order_button(self):
        self.driver.execute_script('arguments[0].click();', self.get_confirm_order_button())


    # METHODS

    """Input Contact Info"""
    def input_contact_info(self):
        self.input_full_name()
        self.input_email()
        self.input_phone_number()


    """ Self-pickup """
    # Самовывоз


    """ Delivery """
    """Input Delivery Info (Address)"""
    def input_delivery_info(self):
        self.input_city_address()
        self.input_entrance()
        self.input_floor()
        self.input_apartment()
        self.click_address_confirm_button()

    """ Set datetime delivery """
    def set_datetime_delivery(self):
        self.click_day_to_delivery_button()
        self.click_choice_time_delivery_button()

    def delivery_method(self):
        self.input_delivery_info()
        self.set_datetime_delivery()


    """ Express Delivery """
    # Экспресс-доставка


    """ Checkout """
    def checkout_information(self):
        self.show_checkout_information()
        self.show_final_price()



    """ Main """
    def buy_product(self, preparation: str):
        self.input_contact_info()
        self.click_preparation_method_button(preparation)
        if preparation == 'Самовывоз':
            pass
        if preparation == 'Доставка':
            self.delivery_method()
        if preparation == 'Экспресс доставка':
            self.delivery_method()
        self.click_payment_button()
        self.checkout_information()
        # self.click_confirm_order_button()