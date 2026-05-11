from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


from base.base_class import Base
class MainPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    """Check"""
    expected_title_mac_page = 'Mac'
    expected_mac_page_url = 'https://pitergsm.ru/catalog/mac/'
    current_title_mac_page_xpath = '//h1[@class="catalog__title"]'

    expected_title_audio_page = 'Аудио'
    expected_audio_page_url = 'https://pitergsm.ru/catalog/audio/'
    current_title_audio_page_xpath = '//h1[@class="catalog__title"]'


    # Locators

    cookie_button = '//button[@id="cookie-consent-btn"]'

    menu_category_mac_button_xpath = '(//a[@class="hcat__link js_hcat-sub-trigger"])[3]'

    menu_category_audio_button_xpath = '(//a[@class="hcat__link js_hcat-sub-trigger"])[5]'


    # Getters

    """Cookie"""
    def get_cookie_button(self):
        return self.wait.until(ec.element_to_be_clickable((By. XPATH, self.cookie_button)))

    """Take Mac"""
    def get_category_mac_button(self):
        return self.wait.until((ec.element_to_be_clickable((By. XPATH, self.menu_category_mac_button_xpath))))

    def get_current_title_mac_page(self):
        return self.wait.until((ec.visibility_of_element_located((By. XPATH, self.current_title_mac_page_xpath))))

    """Take Headphone"""
    def get_category_audio_button(self):
        return self.wait.until(ec.element_to_be_clickable((By.XPATH, self.menu_category_audio_button_xpath)))

    def get_current_title_audio_page(self):
        return self.wait.until(ec.visibility_of_element_located((By. XPATH, self.current_title_audio_page_xpath)))


    # Actions

    """Cookie"""
    def click_cookie_button(self):
        self.get_cookie_button().click()
        print('Click Cookie Button')

    """Take Mac"""
    def click_category_mac_button(self):
        self.get_category_mac_button().click()
        print('Click Menu Category Button')

    """Take Headphone"""
    def click_category_audio_button(self):
        self.get_category_audio_button().click()
        print('Click Menu Audio Button')


    # Methods

    """Take Mac"""
    def select_category_mac(self):
        self.get_current_url()
        self.click_cookie_button()
        self.click_category_mac_button()
        self.assert_word(expected_word=self.expected_title_mac_page, current_word=self.get_current_title_mac_page())
        self.assert_url(expected_url=self.expected_mac_page_url)

    """Take Headphone"""
    def select_category_audio(self):
        self.get_current_url()
        self.click_cookie_button()
        self.click_category_audio_button()
        self.assert_word(expected_word=self.expected_title_audio_page, current_word=self.get_current_title_audio_page())
        self.assert_url(expected_url=self.expected_audio_page_url)