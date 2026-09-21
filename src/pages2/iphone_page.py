import allure

from base.filter_class import Filter
from src.pages2.catalog_page import CatalogPage
from utilities.logger import Logger


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
            Logger.add_start_method(method='filter_iphone')
            non_empty_args = self.get_arguments_non_empty(locals())

            print(non_empty_args)

            self.filter.click_filter_button_if_visible()
            self.filter.click_filter_memory(memory)
            self.filter.click_filter_ram(ram)
            self.filter.set_color(color)
            self.filter.click_filter_confirm()
            self.assertion_products_title(key_word=non_empty_args, product_titles_list=self.get_product_titles(self.product_titles_xpath))
            Logger.add_end_method(current_url=self.get_current_url(),method='filter_iphone')

