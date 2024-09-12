"""
Задание №5
📌 Дорабатываем задачу 4.
📌 Добавьте возможность запуска из командной строки.
📌 При этом значение любого параметра можно опустить.
В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
📌 *Научите функцию распознавать не только текстовое названия дня недели и месяца,
но и числовые, т.е не мая, а 5.
"""

import argparse
from datetime import date, datetime, timedelta, time
import locale

DAYS_OF_WEEK_NUM = {"понедельник": 1, "вторник": 2, "среда": 3, "четверг": 4, "пятница": 5, "суббота": 6,
                    "воскресенье": 7}


def get_date(day: int, day_of_week: int, month: int) -> datetime:
    try:
        dt = get_first_day_of_month(month)
        dt = get_first_needed_day_of_week(dt, day_of_week)
        dt = get_needed_day_of_week(dt, day)
        return dt
    except Exception:
        print("Что-то пошло не так...")


def get_first_day_of_month(month: int) -> datetime:
    year = datetime.now().year
    dt = datetime(year=year, month=month, day=1)
    return dt


def get_first_needed_day_of_week(dt: datetime, day_of_week: int) -> datetime:
    delta_t = timedelta(days=1)
    while not DAYS_OF_WEEK_NUM.get(dt.strftime("%A").lower()) == day_of_week:
        dt += delta_t
    return dt


def get_needed_day_of_week(dt: datetime, day: int) -> datetime:
    delta_t = timedelta(weeks=1)
    for _ in range(1, day):
        dt += delta_t
    return dt


locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
parser = argparse.ArgumentParser(description='Поиск нужного дня недели')
parser.add_argument('--day')
parser.add_argument('--day_of_week')
parser.add_argument('--month')
args = parser.parse_args()
if args.day is None:
    args.day = 1
if args.day_of_week is None:
    args.day_of_week = DAYS_OF_WEEK_NUM.get(datetime.now().strftime("%A").lower())
if args.month is None:
    args.month = datetime.now().month


print(args.day, args.day_of_week, args.month)
print(get_date(args.day, args.day_of_week, args.month))
