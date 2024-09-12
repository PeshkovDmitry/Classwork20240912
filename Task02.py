"""
Задание №2
📌 На семинаре про декораторы был создан логирующий декоратор.
Он сохранял аргументы функции и результат её работы в файл.
📌 Напишите аналогичный декоратор, но внутри используйте модуль logging.
"""

import logging
from typing import Callable


def mylogger(func: Callable) -> Callable:

    def wrapper(*args, **kwargs):
        global logger
        res = func(*args, **kwargs)
        logger.info(f" {args[0]} / {args[1]} = {res}")
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