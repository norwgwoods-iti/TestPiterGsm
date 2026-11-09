import logging
from src.pages2.main_page import MainPage


def test_log_details(driver, caplog):
    caplog.set_level(logging.INFO)

    main_page = MainPage(driver)
    main_page.open_url()

    # Ищем нужную запись
    cookie_logs = [r for r in caplog.records if 'Cookie' in r.message]


    assert len(cookie_logs) == 1
    assert cookie_logs[0].levelname == 'INFO'
    assert cookie_logs[0].name == 'src.pages2.main_page'  # проверили, откуда пришёл лог