"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    delta_yesterday = timedelta(days=1)
    dt_yesterday = datetime.now() - delta_yesterday
    dt_yesterday = dt_yesterday.strftime('%d.%m.%Y')
    print(f'Вчера: {dt_yesterday}')

    dt_now = datetime.now().strftime('%d.%m.%Y')
    print(f'Сегодня: {dt_now}')

    delta_month_ago = timedelta(days=30)
    dt_month_ago = datetime.now() - delta_month_ago
    dt_month_ago = dt_month_ago.strftime('%d.%m.%Y')
    print(f'Месяц назад: {dt_month_ago}')

    dt_string = "01/01/20 12:10:03.234567"
    dt_date = datetime.strptime(dt_string, ('%d/%m/%y %H:%M:%S.%f'))
    print(dt_date)
    
if __name__ == "__main__":
    main()