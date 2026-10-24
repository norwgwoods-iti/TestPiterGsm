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
            memory: str | None = None,
            ram: str | None = None,
            color: str | None = None,
    ):
        with allure.step('Filter iPhone'):
            logger.info('<-- Start Filter iPhone')
            non_empty_args = self.get_arguments_non_empty(locals())

            logger.info(non_empty_args)

            self.filter.click_filter_button_if_visible()
            self.filter.click_filter_memory(memory)
            self.filter.click_filter_ram(ram)
            self.filter.set_color(color)
            self.filter.click_filter_confirm()
            self.assertion_products_title(key_word=non_empty_args, product_titles_list=self.get_product_titles(self.product_titles_xpath))
            logger.info('<-- End Filter iPhone. %s', self.get_current_url())

