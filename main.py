from application.db.people import get_employess
from application.salary import calculate_salary
from my_time import datetime, date, time
from my_time import my_time
import vk


if __name__ == '__main__' :
    print()
    now_time = datetime.today()
    raznost = now_time - my_time
    print('Сегодня ', now_time.strftime('%A, %d %B %Y '))
    print('Домашняя работа проверена через ', raznost, 'после получения')
    print()
    calculate_salary()
    get_employess()