from datetime import datetime
import os

class Logger:
    file_name = f'.\\logs\\log_{datetime.now().strftime("%Y.%m.%d %H-%M-%S")}.log'

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_start_method(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data = f'-------\n'
        data += f'Test name: {test_name}\n'
        data += f'Start time: {datetime.now().strftime("%Y.%m.%d %H-%M-%S")}\n'
        data += f'Start test method: {method}\n'
        data += '\n'

        cls.write_log_to_file(data)


    @classmethod
    def add_end_method(cls, method: str, current_url: str):
        data = f'End time: {datetime.now().strftime("%Y.%m.%d %H-%M-%S")}\n'
        data += f'End method: {method}\n'
        data += f'URL: {current_url}\n'
        data += '-------\n'

        cls.write_log_to_file(data)