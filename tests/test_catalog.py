import allure
import pytest


from src.pages.main_page import MainPage
from src.pages.mac_page import MacPage
from src.pages.audio_page import AudioPage
from src.pages.headphones_page import HeadphonePage
from src.pages.imac_page import IMacPage
from src.pages.cart_page import CartPage

@allure.epic("Internet-shop PiterGSM")
@allure.feature("Catalog")
class TestCatalog:

    base_url = "https://pitergsm.ru/"

    @allure.title('Check Send Field')
    @pytest.mark.regression
    def test_send_search(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Check Send Field')

        main_page = MainPage(driver)
        main_page.search_product(product_name='she')


    @allure.title("Search iMac")
    @pytest.mark.regression
    def test_search_imac(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Search iMac')

        main_page = MainPage(driver)
        main_page.search_product(product_name="iMac")


    @allure.title("Search headphones")
    @pytest.mark.regression
    def test_search_headphones(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Search headphones')

        main_page = MainPage(driver)
        main_page.search_product("Наушники")


    @allure.title("Open Mac category")
    @pytest.mark.regression
    def test_open_mac_category(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Open Mac category')

        main_page = MainPage(driver)
        main_page.select_category_mac()


    @allure.title("Open Audio category")
    @pytest.mark.regression
    def test_open_audio_category(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Open Audio category')

        main_page = MainPage(driver)
        main_page.select_category_audio()


    @allure.title("Open iMac category")
    @pytest.mark.regression
    def test_open_imac_category(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Open iMac category')

        main_page = MainPage(driver)
        main_page.select_category_mac()

        mac_page = MacPage(driver)
        mac_page.select_category_imac()


    @allure.title("Open headphones category")
    @pytest.mark.regression
    def test_open_headphones_category(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Open headphones category')

        main_page = MainPage(driver)
        main_page.select_category_audio()

        category_headphones = 'Наушники'

        audio_page = AudioPage(driver)
        audio_page.select_category_headphones(category=category_headphones)


    @allure.title("Filter iMac by 256 GB")
    @pytest.mark.regression
    def test_filter_imac_by_memory(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Filter iMac by 256 GB')

        main_page = MainPage(driver)
        main_page.select_category_mac()

        mac_page = MacPage(driver)
        mac_page.select_category_imac()

        data_memory_size = '512GB'

        imac_page = IMacPage(driver)
        imac_page.filter_imac_by_memory(memory=data_memory_size)


    @allure.title("Add iMac to cart")
    @pytest.mark.regression
    def test_add_imac_to_cart(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Add iMac to cart')

        main_page = MainPage(driver)
        main_page.select_category_mac()

        mac_page = MacPage(driver)
        mac_page.select_category_imac()

        imac_page = IMacPage(driver)
        imac_page.add_imac_to_cart()


    @allure.title("Filter headphones by Marshall")
    @pytest.mark.regression
    def test_filter_headphones_by_brand(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test - Filter headphones by Marshall')

        main_page = MainPage(driver)
        main_page.select_category_audio()

        category_headphones = 'Наушники'

        audio_page = AudioPage(driver)
        audio_page.select_category_headphones(category_headphones)

        headphones_page = HeadphonePage(driver)

        filter_brand_marshall = 'Marshall'

        headphones_page.click_filter_button_if_visible()
        headphones_page.click_filter_brand(filter_brand=filter_brand_marshall)
        headphones_page.click_filter_confirm()

        assert driver.current_url == AudioPage.expected_headphones_page_url

    @allure.title("Open checkout page")
    @pytest.mark.regression
    def test_checkout_page(self, set_up):

        driver = set_up
        driver.get(self.base_url)

        main_page = MainPage(driver)
        main_page.select_category_audio()

        audio_page = AudioPage(driver)
        category_headphones = 'Наушники'
        audio_page.select_category_headphones(category=category_headphones)

        headphones_page = HeadphonePage(driver)
        filter_brand_apple = 'Apple'
        headphones_page.filter_and_add_headphones_to_cart(filter_brand=filter_brand_apple)

        cart_page = CartPage(driver)
        cart_page.select_order()
