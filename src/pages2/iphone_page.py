from base.filter_class import Filter
from pages2.category_page import CategoryPage


class IphonePage(CategoryPage):
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

        non_empty_args = self.get_arguments_non_empty(locals())

        print(non_empty_args)

        self.filter.click_filter_button_if_visible()
        self.filter.click_filter_memory(memory)
        self.filter.click_filter_ram(ram)
        self.filter.set_color(color)
        self.filter.click_filter_confirm()

        self.assertion_products_title(key_word=non_empty_args, product_titles_list=self.get_product_titles(self.product_titles_xpath))

