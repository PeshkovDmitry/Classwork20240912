"""
Задание №4
📌 Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
📌 Преобразуйте его в дату в текущем году.
📌 Логируйте ошибки, если текст не соответсвует формату.
"""

from datetime import date, datetime, timedelta, time
import locale

DAYS_OF_WEEK_NUM = {"понедельник": 1, "вторник": 2, "среда": 3, "четверг": 4, "пятница": 5, "суббота": 6,
                    "воскресенье": 7}


def get_date(text: str) -> datetime:
    try:
        text = correct_text(text)
        dt = get_first_day_of_month(text)
        dt = get_first_needed_day_of_week(dt, text)
        dt = get_needed_day_of_week(dt, text)
        return dt
    except Exception:
        print("Что-то пошло не так...")


def get_needed_day_of_week(dt, text):
    delta_t = timedelta(weeks=1)
    for _ in range(1, int(text.split()[0])):
        dt += delta_t
    return dt


def correct_text(text):
    text = text.replace("-й", "")
    text = text.replace("-я", "")
    return text


def get_first_day_of_month(text):
    month = text.split()[2]
    month_num = datetime.strptime(month, "%B").month
    year = datetime.now().year
    dt = datetime(year=year, month=month_num, day=1)
    return dt


def get_first_needed_day_of_week(dt, text):
    delta_t = timedelta(days=1)
    while not dt.strftime("%A").lower() == text.split()[1].lower():
        dt += delta_t
    return dt


locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))
input_text = "3-я среда мая"
print(get_date(input_text))
