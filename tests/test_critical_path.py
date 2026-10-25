import allure
import pytest

from src.pages2.order_page import OrderPage
from src.pages2.main_page import MainPage
from src.pages2.iphone_page import IphonePage
from src.pages2.cart_page import CartPage
from tests.test_data.catalog_data import IPHONE_TEST_DATA
import logging

logger = logging.getLogger(__name__)


@allure.epic('Internet-shop PiterGSM')
@allure.feature('Main Page')
class TestMain:

    @allure.title('Check Buy iPhone')
    @pytest.mark.critical_path
    @pytest.mark.parametrize(
        'catalog, memory_size, color', IPHONE_TEST_DATA,
    )
    def test_buy_product(self, driver, catalog:str, memory_size:str, color:str, caplog):
        logger.info(f'Test Buy "{catalog}"')
        caplog.set_level(logging.INFO)

        main_page = MainPage(driver)
        main_page.open_url()
        main_page.select_menu_catalog('iPhone')

        assert 'Start Open main page' in caplog.text

        iphone_page = IphonePage(driver)
        iphone_page.select_product_in_menu_catalog(catalog=catalog)
        iphone_page.filter_iphone(memory=memory_size, color=color)
        iphone_page.add_product_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_order_button()

        order_page = OrderPage(driver)
        order_page.buy_product(preparation='Доставка')





