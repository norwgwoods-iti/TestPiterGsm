from selenium.webdriver.common.by import By

from base.base_class import Base
from selenium.webdriver.support import expected_conditions as ec


class Filter(Base):
    """ Method Filtration """
    # Locators
    filter_color_dropdown_xpath = '//span[@class="filter__title"][contains(text(), "Цвет")]'

    @staticmethod
    def filter_set_color_xpath(color):
        return f'//label[@data-tooltip="{color}"]'

    filter_confirm_xpath = '//button[@id="modef"]'

    # Getters

    def get_filter_memory(self, memory: str | None = None):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, f'//label[@data-tooltip="{memory}"]')))

    def get_filter_ram(self, ram: str | None = None):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, f'//label[@data-tooltip="{ram}"]')))

    def get_filter_color_dropdown(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filter_color_dropdown_xpath)))

    def get_filter_color(self, color: str | None = None):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filter_set_color_xpath(color))))

    def get_filter_confirm(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.filter_confirm_xpath)))

    # Actions

    def click_filter_memory(self, memory: str | None = None):
        if not memory:
            return
        self.driver.execute_script('arguments[0].click();', self.get_filter_memory(memory))
        print('Click filter memory')

    def click_filter_ram(self, ram: str | None = None):
        if not ram:
            return
        self.driver.execute_script('arguments[0].click();', self.get_filter_ram(ram))
        print('Click filter ram')

    def click_filter_color_dropdown(self):
        self.driver.execute_script('arguments[0].click();', self.get_filter_color_dropdown())
        print('Click filter color dropdown')

    def click_filter_color(self, color: str | None = None):
        if not color:
            return
        self.driver.execute_script('arguments[0].click();', self.get_filter_color(color))
        print('Click filter color')

    def click_filter_confirm(self):
        self.driver.execute_script('arguments[0].click();', self.get_filter_confirm())
        print('Click filter confirm')

    # Methods

    def set_color(self, color: str | None = None):
        self.click_filter_color_dropdown()
        self.click_filter_color(color)

    # def filter_product(
    #         self,
    #         memory: str | None = None,
    #         ram: str | None = None,
    #         color: str | None = None, ):
    #     self.click_filter_button_if_visible()
    #     self.click_filter_memory(memory)
    #     self.click_filter_ram(ram)
    #     self.set_color(color)
    #     self.click_filter_confirm()