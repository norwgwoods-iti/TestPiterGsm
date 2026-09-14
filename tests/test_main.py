import allure
import pytest

from pages.audio_page import AudioPage
from pages.mac_page import MacPage
from src.pages.main_page_2 import MainPage
# from src.pages.mac_page import MacPage
from src.base.base_class import Base
from tests.test_data.catalog_data import CATEGORIES


@allure.epic('Internet-shop PiterGSM')
@allure.feature('Main Page')
class TestMain:

    @allure.title('Select Category')
    @pytest.mark.parametrize(
        'category, page_class', CATEGORIES
    )
    def test_select_catalog(self, driver, category: str, page_class):
        print('Test Select Category')

        main_page = MainPage(driver)
        main_page.open_url()
        main_page.select_menu_catalog(category)

        category_page = page_class(driver)






