import allure
from faker import Faker
import pytest

from src.pages.audio_page import AudioPage
from src.pages.cart_page import CartPage
from src.pages.headphones_page import HeadphonePage
from src.pages.imac_page import IMacPage
from src.pages.mac_page import MacPage
from src.pages.main_page import MainPage
from src.pages.order_page import OrderPage


@allure.epic('Internet-shop PiterGSM')
@allure.feature('Buy Product')
class TestBuyProduct:

    base_url = 'https://pitergsm.ru/'

    @allure.title('Check Buy Imac')
    # @pytest.mark.critical
    def test_buy_product_imac(self, set_up):
        driver = set_up

        driver.get(self.base_url)

        print('Test Buy Imac')

        main_page = MainPage(driver)
        main_page.select_category_mac()

        mac_page = MacPage(driver)
        mac_page.select_category_imac()

        data_memory_size = '256GB'

        imac_page = IMacPage(driver)
        imac_page.filter_and_add_imac_to_cart(memory=data_memory_size)

        cart_page = CartPage(driver)
        cart_page.select_order()

        f = Faker('ru_RU')
        city_address = 'Санкт-Петербург, Есенина, д1'
        entrance = 7
        floor = 3
        apartment = 456

        order_page = OrderPage(driver)
        order_page.input_information(full_name=f.name(), email=f.email(), phone_number=f.phone_number())

        """Add Delivery"""
        order_page.input_delivery_information(city_address=city_address,entrance=entrance,floor=floor,apartment=apartment)
        order_page.checkout_information()


    @allure.title('Check Buy Marshall')
    # @pytest.mark.smoke
    def test_buy_product_marshall(self, set_up):

        driver = set_up

        driver.get(self.base_url)

        print('Test Buy Marshall')

        main_page = MainPage(driver)
        main_page.select_category_audio()

        category_headphones = 'Наушники'

        audio_page = AudioPage(driver)
        audio_page.select_category_headphones(category=category_headphones)

        filter_brand_marshall = 'Marshall'

        headphone_page = HeadphonePage(driver)
        headphone_page.filter_and_add_headphones_to_cart(filter_brand=filter_brand_marshall)

        cart_page = CartPage(driver)
        cart_page.select_order()


        f = Faker('ru_RU')
        order_page = OrderPage(driver)
        order_page.input_information(full_name=f.name(), email=f.email(), phone_number=f.phone_number())
        """No delivery"""
        order_page.checkout_information()