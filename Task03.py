"""
Задание №3
📌 Доработаем задачу 2.
📌 Сохраняйте в лог файл раздельно:
○ уровень логирования,
○ дату события,
○ имя функции (не декоратора),
○ аргументы вызова,
○ результат.
"""

import logging
from datetime import date
from typing import Callable


def mylogger(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        global logger
        res = func(*args, **kwargs)
        logger.info(f" Уровень логирования: {logger.level}")
        logger.info(f" Текущая дата: {date.today()}")
        logger.info(f" Имя функции: {func.__name__}")
        logger.info(f" Агрументы: {[arg for arg in args]}")
        logger.info(f" Результат: {res}")
        return res

    return wrapper


@mylogger
def div(a: float, b: float):
    if not b == 0:
        return a / b
    else:
        return "На ноль делить нельзя!"


logging.basicConfig(level=logging.NOTSET, filename="Task01.txt")
logger = logging.getLogger(__name__)
print(div(5, 2))