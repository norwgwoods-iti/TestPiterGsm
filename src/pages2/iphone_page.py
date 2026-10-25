import allure

from base.filter_class import Filter
from src.pages2.catalog_page import CatalogPage
import logging

logger = logging.getLogger(__name__)


class IphonePage(CatalogPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.filter = Filter(driver)


    # Methods
    """ Filter iPhone """
    def filter_iphone(
            self,
            *,
            memory_size: str | None = None,
            ram: str | None = None,
            color: str | None = None,
    ):
        with allure.step('Filter iPhone'):
            logger.info('<-- Start Filter iPhone')
            filters = [
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
            self.assertion_products_title(
                key_word=applied,
                product_title=self.get_product_title(self.product_title_xpath)
            )
            logger.info('<-- End Filter iPhone. %s', self.get_current_url())

