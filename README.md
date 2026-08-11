# Automated E-Commerce UI Test Suite (PiterGSM)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-Latest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)

Автоматизированный фреймворк для сквозного (E2E) UI-тестирования интернет-магазина **PiterGSM**. Проект реализован на языке **Python** с использованием **Pytest** и **Selenium WebDriver** по шаблону проектирования **Page Object Model (POM)**.

---

## 🛠 Технологический стек

* **Language:** Python 3.10+
* **Testing Framework:** Pytest
* **Browser Automation:** Selenium WebDriver
* **Architecture:** Page Object Model (POM)
* **Logging:** Custom logger module (`utilities/logger.py`)
* **Artifacts:** Automatic screenshots & execution logs

---

## 📁 Структура проекта

```text
.
├── base/                   # Базовые классы и общие методы работы со страницей
│   ├── __init__.py
│   └── base_class.py       # Base Page класс (драйвер, логирование, скриншоты)
├── logs/                   # Логи выполнения тестов
│   └── __init__.py
├── pages/                  # Page Object классы для страниц сайта
│   ├── __init__.py
│   ├── main_page.py        # Главная страница
│   ├── mac_page.py         # Раздел Mac
│   ├── imac_page.py        # Страница товара iMac
│   ├── audio_page.py       # Раздел Аудио
│   ├── headphones_page.py  # Страница наушников
│   ├── cart_page.py        # Корзина
│   └── order_page.py       # Оформление заказа
├── screen/                 # Скриншоты прогона
│   └── __init__.py
├── tests/                  # Тестовые сценарии и конфигурации
│   ├── __init__.py
│   ├── conftest.py         # Pytest фикстуры (инициализация/закрытие WebDriver)
│   └── test_buy_product.py # E2E-тест покупки товара
├── utilities/              # Вспомогательные утилиты
│   ├── __init__.py
│   └── logger.py           # Модуль кастомного логирования
└── requirements.txt        # Зависимости проекта
