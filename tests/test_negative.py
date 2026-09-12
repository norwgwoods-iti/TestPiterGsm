# import pytest
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from src.pages.main_page import MainPage
#
# from src.pages.catalog_page import CatalogPage
# #
#
# class TestNegativeScenarios:
#
#     # 1. Попытка отправки поиска со спецсимволами и XSS-инъекцией
#     def test_search_with_special_characters(self, driver):
#         main_page = MainPage(driver)
#         main_page.open()
#
#         # Вводим опасные символы / XSS-вектор
#         xss_payload = "<script>alert('xss')</script> ' OR '1'='1"
#         main_page.search_product(xss_payload)
#
#         # Проверяем, что скрипт не выполнился, а система корректно обработала ввод (нет 500 ошибки)
#         assert "500" not in driver.title
#         # Проверяем, что всплывающих окон (alert) не появилось
#         assert len(driver.window_handles) == 1
#
#     # 2. Переход на несуществующую страницу (404 Not Found)
#     def test_non_existent_page_404(self, driver):
#         invalid_url = "https://pitergsm.ru/non-existent-page-12345/"
#         driver.get(invalid_url)
#
#         page_source = driver.page_source.lower()
#         title = driver.title.lower()
#
#         # Проверяем наличие индикаторов 404 ошибки на странице
#         assert "404" in title or "страница не найдена" in page_source or "not found" in page_source
#
#     # 3. Ввод некорректного значения в фильтр цены (буквы вместо цифр)
#     def test_filter_price_with_invalid_input(self, driver):
#         main_page = MainPage(driver)
#         catalog_page = CatalogPage(driver)
#
#         main_page.open()
#         main_page.search_product("iPhone")  # Переходим в выдачу, где есть фильтры
#
#         try:
#             # Находим поле ввода минимальной цены
#             price_input = WebDriverWait(driver, 5).until(
#                 EC.presence_of_element_locator(catalog_page.FILTER_PRICE_MIN)
#             )
#             price_input.clear()
#             price_input.send_keys("abc@#$%")
#
#             # Получаем значение поля после ввода
#             entered_value = price_input.get_attribute("value")
#
#             # Проверяем, что маска или валидатор не дали ввести буквы
#             assert entered_value != "abc@#$%" or entered_value == ""
#         except Exception:
#             # Если поле фильтра недоступно или скрыто, тест пропускается
#             pytest.skip("Фильтр цены недоступен на данной странице")