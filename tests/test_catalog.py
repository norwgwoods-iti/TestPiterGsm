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
    @pytest.mark.parametrize(
        'product_name', [
            'iMac',
            'Наушники'
        ],
        ids=[
            'existing_product',
            'existing_product'
        ]
        )
    def test_send_search(self, driver, product_name):
        driver = driver
        driver.get(self.base_url)

        print(f'Test - Search "{product_name}"')

        main_page = MainPage(driver)
        main_page.search_product(product_name=product_name)

        main_page.get_screenshot()

    @allure.title('Check Send Field Non Existing Product')
    @pytest.mark.negative
    @pytest.mark.parametrize(
        'product_name', [
            'she',
        ],
        ids=[
            'non_existing_product',
        ],
        )
    def test_send_search_non_existing_product(self, driver, product_name):
        driver = driver
        driver.get(self.base_url)

        print(f'Test - Search "{product_name}"')

        main_page = MainPage(driver)
        main_page.search_product(product_name=product_name)

        main_page.get_screenshot()


    @allure.title("Open Mac category")
    @pytest.mark.regression
    def test_open_mac_category(self, driver):
        driver = driver
        driver.get(self.base_url)

        print('Test - Open Mac category')

        main_page = MainPage(driver)
        main_page.select_category_mac()

        main_page.get_screenshot()


    @allure.title("Open Audio category")
    @pytest.mark.regression
    def test_open_audio_category(self, driver):
        driver = driver
        driver.get(self.base_url)

        print('Test - Open Audio category')

        main_page = MainPage(driver)
        main_page.select_category_audio()

        main_page.get_screenshot()


    @allure.title("Open iMac category")
    @pytest.mark.regression
    def test_open_imac_category(self, driver):
        driver = driver
        driver.get(self.base_url)

        print('Test - Open iMac category')

        main_page = MainPage(driver)
        main_page.select_category_mac()

        mac_page = MacPage(driver)
        mac_page.select_category_imac()

        main_page.get_screenshot()


    @allure.title("Open headphones category")
    @pytest.mark.regression
    @pytest.mark.parametrize('category_audio', ['Наушники', 'Микрофон'])
    def test_open_headphones_category(self, driver, category_audio):
        driver = driver
        driver.get(self.base_url)

        print(f'Test - Open "{category_audio}" category')

        main_page = MainPage(driver)
        main_page.select_category_audio()

        audio_page = AudioPage(driver)
        audio_page.select_subcategory(category=category_audio)

        audio_page.get_screenshot()


    @allure.title("Filter iMac by 512GB")
    @pytest.mark.regression
    @pytest.mark.parametrize('data_memory_size', ['512GB', '256GB'])
    def test_filter_imac_by_memory(self, driver, data_memory_size):
        driver = driver
        driver.get(self.base_url)

        print(f'Test - Filter iMac by {data_memory_size}')

        main_page = MainPage(driver)
        main_page.select_category_mac()

        mac_page = MacPage(driver)
        mac_page.select_category_imac()

        imac_page = IMacPage(driver)
        imac_page.filter_imac_by_memory(memory=data_memory_size)

        imac_page.get_screenshot()


    @allure.title("Add iMac to cart")
    @pytest.mark.regression
    def test_add_imac_to_cart(self, driver):
        driver = driver
        driver.get(self.base_url)

        print('Test - Add iMac to cart')

        main_page = MainPage(driver)
        main_page.select_category_mac()

        mac_page = MacPage(driver)
        mac_page.select_category_imac()

        imac_page = IMacPage(driver)
        imac_page.add_imac_to_cart()

        imac_page.get_screenshot()


    @allure.title("Filter headphones by Marshall")
    @pytest.mark.regression
    @pytest.mark.parametrize(
        'filter_brand',
        [
            'Marshall',
            'JBL'
        ],
        ids=[
            'Marshall',
            'JBL'
        ]

    )
    def test_filter_headphones_by_brand(self, driver, filter_brand):
        driver = driver
        driver.get(self.base_url)

        print(f'Test - Filter "Наушники" by "{filter_brand}"')

        main_page = MainPage(driver)
        main_page.select_category_audio()

        audio_page = AudioPage(driver)
        audio_page.select_subcategory(category='Наушники')

        headphones_page = HeadphonePage(driver)

        headphones_page.click_filter_button_if_visible()
        headphones_page.click_filter_brand(filter_brand=filter_brand)
        headphones_page.click_filter_confirm()

        headphones_page.assertion_products_title(
            key_word=filter_brand,
            product_titles_list=headphones_page.product_titles_xpath
        )

        headphones_page.get_screenshot()


    @allure.title("Open checkout page")
    @pytest.mark.regression
    def test_checkout_page(self, driver):
        driver = driver
        driver.get(self.base_url)

        print('Test - Open checkout page')

        main_page = MainPage(driver)
        main_page.select_category_audio()

        audio_page = AudioPage(driver)
        category_headphones = 'Наушники'
        audio_page.select_subcategory(category=category_headphones)

        headphones_page = HeadphonePage(driver)
        filter_brand_apple = 'Apple'
        headphones_page.filter_and_add_headphones_to_cart(filter_brand=filter_brand_apple)
        headphones_page.assertion_products_title(key_word=filter_brand_apple, product_titles_list=headphones_page.product_titles_xpath)

        cart_page = CartPage(driver)
        cart_page.select_order()

        cart_page.get_screenshot()