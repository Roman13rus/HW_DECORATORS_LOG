import os
import logging
# import datetime
def logger(old_function):
    def new_function(*args, **kwargs):
        my_logger = logging.getLogger(__name__)
        my_logger.setLevel(logging.INFO)
        my_handler = logging.FileHandler(f"main.log", mode='a')
        my_formatter = logging.Formatter("%(asctime)s %(message)s")
        my_handler.setFormatter(my_formatter)
        my_logger.addHandler(my_handler)
        res = old_function(*args, **kwargs)
        my_logger.info(f"The function - {old_function.__name__}, accepts arguments  - {args}, {kwargs}, got the result, {res}")
        # my_logger.info(f"{old_function.__name__},{args}, {kwargs}, {res}")
        return res
    return new_function
def test_1():

    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'
    
    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()