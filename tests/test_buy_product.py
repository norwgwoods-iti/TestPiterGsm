from faker import Faker

from pages.audio_page import AudioPage
from pages.cart_page import CartPage
from pages.headphones_page import HeadphonePage
from pages.imac_page import IMacPage
from pages.mac_page import MacPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


def test_buy_product_imac(set_up):

    driver = set_up

    print('Test 1')

    mp = MainPage(driver)
    mp.select_category_mac()

    macp = MacPage(driver)
    macp.select_category_imac()

    imacp = IMacPage(driver)
    imacp.filter_and_add_imac_to_cart()

    cp = CartPage(driver)
    cp.select_order()

    f = Faker('ru_RU')
    city_address = 'Санкт-Петербург, Есенина, д1'
    entrance = 7
    floor = 3
    apartment = 456
    op = OrderPage(driver)
    op.input_information(full_name=f.name(), email=f.email(), phone_number=f.phone_number())
    """Add Delivery"""
    op.input_delivery_information(city_address=city_address,entrance=entrance,floor=floor,apartment=apartment)
    op.checkout_information()

def test_buy_product_marshall(set_up):

    driver = set_up

    print('Test 2')

    mp = MainPage(driver)
    mp.select_category_audio()

    ap = AudioPage(driver)
    ap.select_category_headphones()

    hp = HeadphonePage(driver)
    hp.filter_and_add_headphones_to_cart()

    cp = CartPage(driver)
    cp.select_order()


    f = Faker('ru_RU')
    op = OrderPage(driver)
    op.input_information(full_name=f.name(), email=f.email(), phone_number=f.phone_number())
    """No delivery"""
    op.checkout_information()