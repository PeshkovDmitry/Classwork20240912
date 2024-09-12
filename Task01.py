"""
Задание №1
📌 Напишите программу, которая использует модуль logging для вывода сообщения об ошибке в файл.
📌 Например отлавливаем ошибку деления на ноль.
"""
import logging


def div(a: float, b: float) -> float:
    global logger
    if not b == 0:
        return a / b
    else:
        logger.error("На ноль делить нельзя!")


logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
print(div(5, 0))


