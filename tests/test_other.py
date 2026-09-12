import pytest
import allure

from src.pages.main_page import MainPage
# from pages.catalog_page import CatalogPage
# from pages.cart_page import CartPage


@allure.epic('Internet-shop PiterGSM')
@allure.feature('')
class TestPiterGsm:

    base_url = 'https://pitergsm.ru/'

    @allure.title('Check Open Main Page')
    def test_main_page_title(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test Open Main Page')

        main_page = MainPage(driver)
        main_page.check_assertion_main_title()


    @allure.title('Check Search Valid Product')
    def test_search_valid_product(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test Search Valid Product')

        main_page = MainPage(driver)
        main_page.search_product("iPhone 15")


    @allure.title('Check Search Invalid Product (Negative)')
    def test_search_invalid_product(self, set_up):
        driver = set_up
        driver.get(self.base_url)

        print('Test Search Invalid Product (Negative)')

        main_page = MainPage(driver)
        product_name = "qwertyuiop123456789"
        main_page.find_product(product_name=product_name)

        main_page.assertion_products_title(product_name=product_name)

    #
    # # 5. Добавление товара в корзину из выдачи поиска
    # def test_add_product_to_cart(self, driver):
    #     main_page = MainPage(driver)
    #     catalog_page = CatalogPage(driver)
    #     cart_page = CartPage(driver)
    #
    #     main_page.open()
    #     main_page.search_product("AirPods")
    #     catalog_page.add_first_product_to_cart()
    #
    #     cart_page.open_cart()
    #     assert cart_page.get_cart_items_count() > 0
    #
    # # 6. Удаление товара из корзины
    # def test_remove_product_from_cart(self, driver):
    #     main_page = MainPage(driver)
    #     catalog_page = CatalogPage(driver)
    #     cart_page = CartPage(driver)
    #
    #     main_page.open()
    #     main_page.search_product("Чехол")
    #     catalog_page.add_first_product_to_cart()
    #
    #     cart_page.open_cart()
    #     initial_count = cart_page.get_cart_items_count()
    #     cart_page.remove_first_item()
    #
    #     # Ждем обновления DOM/списка
    #     driver.implicitly_wait(2)
    #     assert cart_page.get_cart_items_count() < initial_count
    #
    # # 7. Проверка наличия кликабельного номера телефона в шапке
    # def test_header_phone_contact(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.open()
    #     phone_elem = driver.find_element(*main_page.PHONE_LINK)
    #     assert phone_elem.is_displayed()
    #     assert "tel:" in phone_elem.get_attribute("href")
    #
    # # 8. Переход по разделам каталога (Navigation Menu)
    # def test_navigate_to_catalog_section(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.open()
    #
    #     catalog_btn = driver.find_element(*main_page.CATALOG_MENU)
    #     catalog_btn.click()
    #
    #     # Проверяем, что URL изменился или открылось меню
    #     assert "catalog" in driver.current_url or catalog_btn.is_displayed()
    #
    # # 9. Проверка отклика формы поиска на пустой ввод
    # def test_empty_search_submit(self, driver):
    #     main_page = MainPage(driver)
    #     main_page.open()
    #
    #     current_url = driver.current_url
    #     main_page.search_product("")
    #
    #     # Страница либо остается той же, либо перенаправляет на поиск без ошибки сервера (не 500)
    #     assert "500" not in driver.title
    #
    # # 10. Проверка открываемости корзины без добавленных товаров
    # def test_empty_cart_view(self, driver):
    #     cart_page = CartPage(driver)
    #     cart_page.open_cart()

        assert cart_page.get_cart_items_count() == 0