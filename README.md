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
* **Reporting:** Allure Framework (`allure-pytest`)
* **Logging:** Custom logger module (`utilities/logger.py`)
* **Artifacts:** Automatic screenshots & execution logs

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone [https://github.com/norwgwoods-iti/TestPiterGsm.git](https://github.com/norwgwoods-iti/TestPiterGsm.git)
cd TestPiterGsm
```

### 2. Настройка виртуального окружения
macOS / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
Windows:

```DOS
python -m venv venv
venv\Scripts\activate
```

### 3. Установка зависимостей

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 🧪 Запуск тестов

### Базовые команды
Запуск всех тестов:
```bash
pytest
```
Запуск с подробным выводом (verbose):
```bash
pytest -v -s
```
Запуск конкретного тестового файла:
```bash
pytest tests/test_buy_product.py -v -s
```
Запуск одной конкретной тестовой функции:
```bash
pytest tests/test_buy_product.py::test_specific_function
```

---

## 📊 Генерация отчетов Allure

Для сбора результатов и просмотра красивых интерактивных графиков используйте интеграцию с Allure.

### 1. Запуск тестов со сбором результатов
Добавьте флаг `--alluredir`, чтобы сохранить промежуточные данные в папку `allure-results`:

```bash
# Прогон всех тестов
pytest --alluredir=allure-results

# Прогон одного конкретного теста
pytest tests/test_buy_product.py::test_specific_function --alluredir=allure-results
```

### 2. Локальный просмотр отчета (Allure Serve)
Чтобы автоматически собрать HTML-отчет во временную папку и мгновенно открыть его в браузере по умолчанию, выполните:

```bash
allure serve allure-results
```
*Для завершения работы локального веб-сервера нажмите `Ctrl + C` в окне терминала.*

### 3. Генерация статического отчета (Опционально)
Если вам нужно сохранить готовый отчет в виде папки с веб-страницами (например, для публикации на GitHub Pages или отправки архивом), соберите его вручную:

```bash
allure generate allure-results -o allure-report --clean
```
* Флаг `-o allure-report` задает конечную папку.
* Флаг `--clean` предварительно очищает старые результаты.

---

### 📊 Логи и скриншоты (без Allure)

- Логи (logs/): Все действия в ходе выполнения шагов (клики, вводы, переход по URL, проверки) фиксируются через utilities/logger.py.
- Скриншоты (screen/): При необходимости снятия снимка экрана (например, подтверждение шага или фиксация состояния) скриншоты автоматически сохраняются с меткой времени в директорию screen/.


## 📁 Структура проекта

```text
TestPiterGsm/
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
```

### 👨‍💻 Автор
GitHub: @norwgwoods-iti

