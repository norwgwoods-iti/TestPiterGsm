from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from base.base_class import Base


class CategoryPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.category_title_xpath = '//h1[@class="catalog__title"]'
        self.product_titles_xpath = '//a[@class="prodcard__name"]'


    # Locators

    @staticmethod
    def button_category_xpath(category):
        return f'//a[@class=" tags__tag"][(text()="{category}")]'


    # Getters
    def get_button_category(self, category):
        return self.wait.until((ec.element_to_be_clickable((By.XPATH, self.button_category_xpath(category)))))

    # Actions
    def click_button_category(self, category):
        self.driver.execute_script('arguments[0].click();', self.get_button_category(category))
        print(f'Select category: "{category}"')


    # Methods

    def select_menu_category(self, category: str):
        self.click_button_category(category)
        self.assert_title(expected_title=category)
        self.assertion_products_title(
            key_word=category,
            product_titles_list=self.get_product_titles(self.product_titles_xpath))

