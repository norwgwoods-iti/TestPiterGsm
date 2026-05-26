import logging

# 1. Простая настройка: говорим, в каком формате выводить сообщения
logging.basicConfig(
    level=logging.DEBUG,  # С какого уровня важности показывать логи
    format='%(asctime)s [%(levelname)s] %(message)s',  # Шаблон строки
    datefmt='%Y-%m-%d %H:%M:%S',  # Формат времени
    filename='py_log.log', filemode='w'
)

# logging.debug('DEBUG Voot')
# logging.info('INFO Shoti')
# logging.warning('WARNING Shoti')
# logging.error('ERROR Shoti')
# logging.critical('CRITICAL Shoti')

# 2. Использование в тестах
def login_test():
    logging.info("Тест запущен. Открываем страницу авторизации...")

    # Симулируем шаг теста
    user_logged_in = False

    if not user_logged_in:
        logging.debug("Не удалось войти в систему! Кнопка профиля не появилась.")


# login_test()

x_vals = [2,3,6,4,10]
y_vals = [5,7,12,0,1]
for x_val,y_val in zip(x_vals,y_vals):
    x,y = x_val,y_val
    logging.info(f'Производим деление {x} на {y}')
    try:
        logging.info(f'Результат равен {x/y}')
    except ZeroDivisionError as err:
        logging.error('ZeroDivisionError', exc_info=True)
