from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from base.base_class import Base


class CategoryPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.catalog_title_xpath = '//h1[@class="catalog__title"]'

    @staticmethod
    def button_category_xpath(category):
        return f'//a[@class=" tags__tag"][contains(text({category}))]'


