import allure
import pytest

from pages.audio_page import AudioPage
from pages.mac_page import MacPage
from src.pages2.main_page_2 import MainPage
from src.pages2.iphone_page import IphonePage
# from src.pages.mac_page import MacPage
from src.base.base_class import Base
from tests.test_data.catalog_data import CATEGORIES, CATALOG


@allure.epic('Internet-shop PiterGSM')
@allure.feature('Main Page')
class TestMain:

    @allure.title('Check Buy iPhone')
    @pytest.mark.parametrize(
        'category, memory_size', [
            ('iPhone 17', '256GB'),
            # ('iPhone 17', '512GB'),
            # ('iPhone 18 Pro Max', '256GB'),
            # ('iPhone 18 Pro Max', '512GB'),
        ]
    )
    def test_select_catalog(self, driver, category:str, memory_size:str):
        print(f'Test Buy {category}')

        main_page = MainPage(driver)
        main_page.open_url()
        main_page.select_menu_catalog('iPhone')

        iphone_page = IphonePage(driver)
        iphone_page.select_menu_category(category=category)

        # iphone_page.filter_product(memory=memory_size, titles_list=iphone_page.product_titles_xpath)

        iphone_page.get_screenshot()




