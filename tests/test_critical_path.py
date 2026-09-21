import allure
import pytest

from src.pages2.order_page import OrderPage
from src.pages2.main_page_2 import MainPage
from src.pages2.iphone_page import IphonePage
from src.pages2.cart_page import CartPage
from tests.test_data.catalog_data import IPHONE_TEST_DATA


@allure.epic('Internet-shop PiterGSM')
@allure.feature('Main Page')
class TestMain:

    @allure.title('Check Buy iPhone')
    @pytest.mark.critical_path
    @pytest.mark.parametrize(
        'catalog, memory_size, color', IPHONE_TEST_DATA,
    )
    def test_select_catalog(self, driver, catalog:str, memory_size:str, color:str):
        print(f'Test Buy "{catalog}"')

        main_page = MainPage(driver)
        main_page.open_url()
        main_page.select_menu_catalog('iPhone')

        iphone_page = IphonePage(driver)
        iphone_page.select_product_in_menu_catalog(catalog=catalog)
        iphone_page.filter_iphone(memory=memory_size, color=color)
        iphone_page.add_product_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_order_button()

        order_page = OrderPage(driver)
        order_page.buy_product(preparation='Доставка')





