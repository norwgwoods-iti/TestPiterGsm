# from pages.category_page import CategoryPage
import logging

import allure

from src.pages2.catalog_page import CatalogPage
from src.base.filter_class import Filter
from src.base.base_class import Base

# class MacPage(CategoryPage):
#     def __init__(self, driver):
#         super().__init__(driver)


CATEGORIES = [
    'MacBook Pro',
    'MacBook Air',
    'MacBook Neo',
    'iMac',
    'Mac mini',
    'Mac Studio',
    'Apple Studio Display',
    'Клавиатуры',
    'Трекпады',
    'Мыши'
]

logger = logging.getLogger(__name__)

class MacPage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.filter = Filter(driver)

    # METHODS
    """ Filter iMac """
    def filter_imac(
        self,
        *,
        screen_size: float | str | None = None,
        memory_size: str | None = None,
        ram: str | None = None,
        color: str | None = None,
    ):
        with allure.step('Filter iMac'):
            logger.info('<-- Start Filter iMac')
            filters = [
                (screen_size, self.filter.click_filter_screen_size),
                (memory_size, self.filter.click_filter_memory),
                (ram, self.filter.click_filter_ram),
                (color, self.filter.set_color),
            ]
            self.filter.click_filter_button_if_visible()
            for value, apply_filter in filters:
                if value:
                    apply_filter(value)
            self.filter.click_filter_confirm()

            applied = [value for value, _ in filters if value]
            Base.assertion_products_title(
                key_word=applied,
                product_title=self.get_product_title(self.product_title_xpath)
            )
            logger.info('<-- End Filter iMac. %s', self.get_current_url())

