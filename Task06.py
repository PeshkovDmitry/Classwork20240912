"""
Задание №6
📌 Напишите код, который запускается из командной строки и получает на вход
путь до директории на ПК.
📌 Соберите информацию о содержимом в виде объектов namedtuple.
📌 Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.
📌 В процессе сбора сохраните данные в текстовый файл используя
логирование.
"""

import argparse
import os
from collections import namedtuple
import logging


def get_path_from_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir')
    args = parser.parse_args()
    if args.dir is None:
        return ""
    else:
        return args.dir


logging.basicConfig(level=logging.NOTSET, filename="Task06.txt")
logger = logging.getLogger(__name__)
directory = get_path_from_args()
Info = namedtuple("Info", "path extension is_directory parent")
for home_dir, cur_dir, cur_file in os.walk(directory):
    for d in cur_dir:
        info = Info(path=d, extension="", is_directory=True, parent=home_dir)
        logger.info(info)
    for f in cur_file:
        if len(f.split(".")) == 2:
            info = Info(path=f.split(".")[0], extension=f.split(".")[1], is_directory=False, parent=home_dir)
        else:
            info = Info(path=f, extension="", is_directory=False, parent=home_dir)
        logger.info(info)

